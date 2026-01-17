#!/usr/bin/env python3
"""
Documentation Scraper - Converts web docs to agent-friendly markdown.

Scrapes documentation websites and converts them to clean markdown files
for use by AI agents. Handles navigation discovery, content extraction,
and markdown cleanup.

Usage:
    uv run python scripts/scrape_docs.py <url> [options]

Examples:
    # Scrape Rerun Python docs
    uv run python scripts/scrape_docs.py https://ref.rerun.io/docs/python/stable/common/ -o docs/external/rerun

    # Scrape with depth limit
    uv run python scripts/scrape_docs.py https://example.com/docs/ -o docs/external/example --max-depth 2

    # Dry run to see what would be scraped
    uv run python scripts/scrape_docs.py https://example.com/docs/ --dry-run
"""

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:
    print("Missing dependencies. Install with:")
    print("  uv pip install requests beautifulsoup4 lxml")
    sys.exit(1)


@dataclass
class PageInfo:
    """Information about a scraped page."""

    url: str
    title: str
    path: str  # relative path in output
    depth: int
    links: list[str] = field(default_factory=list)


@dataclass
class ScrapeConfig:
    """Configuration for scraping."""

    base_url: str
    output_dir: Path
    max_depth: int = 3
    delay: float = 0.5  # seconds between requests
    dry_run: bool = False
    include_patterns: list[str] = field(default_factory=list)
    exclude_patterns: list[str] = field(default_factory=list)
    user_agent: str = "DocScraper/1.0 (AI Agent Documentation Tool)"


class DocScraper:
    """Scrapes documentation sites and converts to markdown."""

    def __init__(self, config: ScrapeConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers["User-Agent"] = config.user_agent
        self.visited: set[str] = set()
        self.pages: list[PageInfo] = []
        self.base_domain = urlparse(config.base_url).netloc
        self.base_path = urlparse(config.base_url).path.rstrip("/")

    def normalize_url(self, url: str) -> str:
        """Normalize URL for comparison."""
        parsed = urlparse(url)
        # Remove fragment and trailing slash
        path = parsed.path.rstrip("/") or "/"
        return f"{parsed.scheme}://{parsed.netloc}{path}"

    def is_valid_url(self, url: str) -> bool:
        """Check if URL should be scraped."""
        parsed = urlparse(url)

        # Must be same domain
        if parsed.netloc != self.base_domain:
            return False

        # Must be under base path
        if not parsed.path.startswith(self.base_path):
            return False

        # Check exclude patterns
        for pattern in self.config.exclude_patterns:
            if re.search(pattern, url):
                return False

        # Check include patterns (if any specified, URL must match one)
        if self.config.include_patterns:
            if not any(re.search(p, url) for p in self.config.include_patterns):
                return False

        return True

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a page."""
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            return BeautifulSoup(resp.text, "lxml")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def extract_links(self, soup: BeautifulSoup, base_url: str) -> list[str]:
        """Extract valid links from page."""
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            # Skip anchors, javascript, mailto
            if href.startswith(("#", "javascript:", "mailto:")):
                continue
            # Resolve relative URLs
            full_url = urljoin(base_url, href)
            normalized = self.normalize_url(full_url)
            if self.is_valid_url(normalized) and normalized not in self.visited:
                links.append(normalized)
        return list(set(links))

    def extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title."""
        # Try common title locations
        for selector in [
            "h1",
            ".md-content h1",
            "article h1",
            ".content h1",
            "main h1",
            "title",
        ]:
            elem = soup.select_one(selector)
            if elem:
                return elem.get_text(strip=True)
        return "Untitled"

    def extract_content(self, soup: BeautifulSoup) -> Optional[Tag]:
        """Extract main content area."""
        # Common content selectors (ordered by specificity)
        selectors = [
            ".md-content__inner",  # MkDocs Material
            ".md-content",
            "article.md-typeset",
            "article",
            ".content",
            ".documentation",
            "main",
            "#content",
            ".post-content",
            ".entry-content",
        ]
        for selector in selectors:
            content = soup.select_one(selector)
            if content:
                return content
        return soup.body

    def clean_content(self, content: Tag) -> Tag:
        """Remove unwanted elements from content."""
        # Elements to remove
        remove_selectors = [
            "nav",
            ".nav",
            ".navigation",
            ".sidebar",
            ".toc",
            ".table-of-contents",
            ".md-nav",
            ".md-sidebar",
            ".md-header",
            ".md-footer",
            ".md-search",
            ".headerlink",
            ".anchor",
            "script",
            "style",
            "iframe",
            ".admonition.todo",
            ".edit-this-page",
            ".feedback",
            ".page-nav",
            ".breadcrumb",
            ".breadcrumbs",
            "[aria-hidden='true']",
        ]

        for selector in remove_selectors:
            for elem in content.select(selector):
                elem.decompose()

        return content

    def html_to_markdown(self, element: Tag, depth: int = 0) -> str:
        """Convert HTML element to markdown."""
        result = []

        for child in element.children:
            if isinstance(child, NavigableString):
                text = str(child)
                if text.strip():
                    result.append(text)
                elif result and not result[-1].endswith(" "):
                    result.append(" ")
                continue

            if not isinstance(child, Tag):
                continue

            tag = child.name

            # Headings
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(tag[1])
                text = child.get_text(strip=True)
                if text:
                    result.append(f"\n\n{'#' * level} {text}\n\n")

            # Paragraphs
            elif tag == "p":
                text = self.html_to_markdown(child, depth)
                if text.strip():
                    result.append(f"\n\n{text.strip()}\n\n")

            # Code blocks
            elif tag == "pre":
                code = child.find("code")
                if code:
                    # Try to get language from class
                    lang = ""
                    classes = code.get("class", [])
                    for cls in classes:
                        if cls.startswith("language-"):
                            lang = cls[9:]
                            break
                        elif cls.startswith("highlight-"):
                            lang = cls[10:]
                            break
                    code_text = code.get_text()
                    result.append(f"\n\n```{lang}\n{code_text.strip()}\n```\n\n")
                else:
                    result.append(f"\n\n```\n{child.get_text().strip()}\n```\n\n")

            # Inline code
            elif tag == "code":
                # Skip if inside pre (handled above)
                if child.parent and child.parent.name == "pre":
                    continue
                text = child.get_text()
                if text:
                    result.append(f"`{text}`")

            # Lists
            elif tag in ("ul", "ol"):
                items = []
                for i, li in enumerate(child.find_all("li", recursive=False)):
                    prefix = "-" if tag == "ul" else f"{i + 1}."
                    item_text = self.html_to_markdown(li, depth + 1).strip()
                    # Handle nested content
                    lines = item_text.split("\n")
                    first_line = lines[0] if lines else ""
                    rest = "\n".join("  " + line for line in lines[1:] if line.strip())
                    items.append(f"{prefix} {first_line}")
                    if rest:
                        items.append(rest)
                if items:
                    result.append("\n\n" + "\n".join(items) + "\n\n")

            # Tables
            elif tag == "table":
                result.append(self.table_to_markdown(child))

            # Links
            elif tag == "a":
                href = child.get("href", "")
                text = child.get_text(strip=True)
                if text and href:
                    # Clean up href
                    if href.startswith("#"):
                        result.append(text)  # Skip anchor-only links
                    else:
                        result.append(f"[{text}]({href})")
                elif text:
                    result.append(text)

            # Bold/Strong
            elif tag in ("strong", "b"):
                text = child.get_text(strip=True)
                if text:
                    result.append(f"**{text}**")

            # Italic/Emphasis
            elif tag in ("em", "i"):
                text = child.get_text(strip=True)
                if text:
                    result.append(f"*{text}*")

            # Divs and other containers - recurse
            elif tag in ("div", "section", "article", "main", "span", "dd", "dt", "dl"):
                inner = self.html_to_markdown(child, depth)
                if inner.strip():
                    result.append(inner)

            # Blockquotes
            elif tag == "blockquote":
                inner = self.html_to_markdown(child, depth).strip()
                if inner:
                    quoted = "\n".join(f"> {line}" for line in inner.split("\n"))
                    result.append(f"\n\n{quoted}\n\n")

            # Horizontal rule
            elif tag == "hr":
                result.append("\n\n---\n\n")

            # Images
            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    result.append(f"![{alt}]({src})")

            # Line breaks
            elif tag == "br":
                result.append("\n")

            # Skip these
            elif tag in ("script", "style", "nav", "header", "footer"):
                continue

            # Default: recurse
            else:
                inner = self.html_to_markdown(child, depth)
                if inner.strip():
                    result.append(inner)

        return "".join(result)

    def table_to_markdown(self, table: Tag) -> str:
        """Convert HTML table to markdown."""
        rows = []
        headers = []

        # Extract headers
        thead = table.find("thead")
        if thead:
            for th in thead.find_all(["th", "td"]):
                headers.append(th.get_text(strip=True))
        else:
            # Try first row
            first_row = table.find("tr")
            if first_row:
                for cell in first_row.find_all(["th", "td"]):
                    headers.append(cell.get_text(strip=True))

        if not headers:
            return ""

        # Build table
        rows.append("| " + " | ".join(headers) + " |")
        rows.append("| " + " | ".join("---" for _ in headers) + " |")

        # Extract body rows
        tbody = table.find("tbody") or table
        for tr in tbody.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            if len(cells) == len(headers):
                row_data = []
                for cell in cells:
                    text = cell.get_text(strip=True).replace("|", "\\|")
                    text = text.replace("\n", " ")
                    row_data.append(text)
                rows.append("| " + " | ".join(row_data) + " |")

        return "\n\n" + "\n".join(rows) + "\n\n"

    def clean_markdown(self, md: str) -> str:
        """Clean up markdown output."""
        # Collapse multiple blank lines
        md = re.sub(r"\n{3,}", "\n\n", md)
        # Remove trailing whitespace
        md = "\n".join(line.rstrip() for line in md.split("\n"))
        # Remove leading/trailing blank lines
        md = md.strip()
        return md

    def url_to_path(self, url: str) -> str:
        """Convert URL to filesystem path."""
        parsed = urlparse(url)
        path = parsed.path

        # Remove base path prefix
        if path.startswith(self.base_path):
            path = path[len(self.base_path) :]

        # Clean up
        path = path.strip("/")
        if not path:
            path = "index"

        # Convert to safe filename
        path = path.replace("/", "_")
        path = re.sub(r"[^\w\-_]", "_", path)
        path = re.sub(r"_+", "_", path)

        return f"{path}.md"

    def scrape_page(self, url: str, depth: int) -> Optional[PageInfo]:
        """Scrape a single page."""
        if depth > self.config.max_depth:
            return None

        normalized = self.normalize_url(url)
        if normalized in self.visited:
            return None

        self.visited.add(normalized)
        print(f"[{depth}] Scraping: {url}")

        if self.config.dry_run:
            return PageInfo(
                url=url, title="(dry run)", path=self.url_to_path(url), depth=depth
            )

        # Rate limiting
        time.sleep(self.config.delay)

        soup = self.fetch_page(url)
        if not soup:
            return None

        title = self.extract_title(soup)
        content = self.extract_content(soup)

        if not content:
            print(f"  No content found for {url}")
            return None

        # Clean and convert
        content = self.clean_content(content)
        markdown = self.html_to_markdown(content)
        markdown = self.clean_markdown(markdown)

        # Extract links for crawling
        links = self.extract_links(soup, url)

        # Determine output path
        rel_path = self.url_to_path(url)

        # Write file
        out_path = self.config.output_dir / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Add metadata header
        header = f"---\nsource: {url}\ntitle: {title}\n---\n\n"
        out_path.write_text(header + markdown)
        print(f"  -> {out_path}")

        return PageInfo(url=url, title=title, path=rel_path, depth=depth, links=links)

    def scrape(self) -> list[PageInfo]:
        """Main scrape entrypoint."""
        print(f"Starting scrape from: {self.config.base_url}")
        print(f"Output directory: {self.config.output_dir}")
        print(f"Max depth: {self.config.max_depth}")

        if not self.config.dry_run:
            self.config.output_dir.mkdir(parents=True, exist_ok=True)

        # BFS crawl
        queue = [(self.config.base_url, 0)]

        while queue:
            url, depth = queue.pop(0)

            page = self.scrape_page(url, depth)
            if page:
                self.pages.append(page)

                # Add linked pages to queue
                for link in page.links:
                    if link not in self.visited:
                        queue.append((link, depth + 1))

        print(f"\nScraped {len(self.pages)} pages")

        # Generate index
        if not self.config.dry_run and self.pages:
            self.generate_index()

        return self.pages

    def generate_index(self):
        """Generate an index file for the scraped docs."""
        index_path = self.config.output_dir / "_index.md"

        lines = [
            "# Documentation Index",
            "",
            f"Source: {self.config.base_url}",
            f"Pages: {len(self.pages)}",
            "",
            "## Pages",
            "",
        ]

        # Sort by depth then title
        sorted_pages = sorted(self.pages, key=lambda p: (p.depth, p.title))
        for page in sorted_pages:
            indent = "  " * page.depth
            lines.append(f"{indent}- [{page.title}]({page.path})")

        index_path.write_text("\n".join(lines))
        print(f"Generated index: {index_path}")

        # Also generate JSON manifest
        manifest_path = self.config.output_dir / "_manifest.json"
        manifest = {
            "source": self.config.base_url,
            "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "pages": [
                {"url": p.url, "title": p.title, "path": p.path, "depth": p.depth}
                for p in sorted_pages
            ],
        }
        manifest_path.write_text(json.dumps(manifest, indent=2))
        print(f"Generated manifest: {manifest_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Scrape documentation websites and convert to markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape Rerun Python docs
  uv run python scripts/scrape_docs.py https://ref.rerun.io/docs/python/stable/common/ -o docs/external/rerun

  # Limit crawl depth
  uv run python scripts/scrape_docs.py https://example.com/docs/ -o docs/ext --max-depth 1

  # Dry run (show what would be scraped)
  uv run python scripts/scrape_docs.py https://example.com/docs/ --dry-run
        """,
    )
    parser.add_argument("url", help="Base URL to start scraping from")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("docs/external"),
        help="Output directory (default: docs/external)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=3,
        help="Maximum crawl depth (default: 3)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between requests in seconds (default: 0.5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be scraped without actually scraping",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Regex patterns for URLs to include (can be repeated)",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Regex patterns for URLs to exclude (can be repeated)",
    )

    args = parser.parse_args()

    config = ScrapeConfig(
        base_url=args.url,
        output_dir=args.output,
        max_depth=args.max_depth,
        delay=args.delay,
        dry_run=args.dry_run,
        include_patterns=args.include,
        exclude_patterns=args.exclude,
    )

    scraper = DocScraper(config)
    pages = scraper.scrape()

    if args.dry_run:
        print("\nDry run complete. Pages that would be scraped:")
        for page in pages:
            print(f"  [{page.depth}] {page.url} -> {page.path}")


if __name__ == "__main__":
    main()
