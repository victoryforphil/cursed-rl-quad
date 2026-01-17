# Documentation Scraper Agent Guide

This folder contains scraped external documentation for agent reference.

## Quick Start

To pull documentation from a website into markdown for agent use:

```bash
# Install dependencies (one time)
uv pip install requests beautifulsoup4 lxml

# Scrape docs
uv run python scripts/scrape_docs.py <URL> -o docs/external/<name>
```

## Examples

### Rerun Python API Docs

```bash
uv run python scripts/scrape_docs.py \
    https://ref.rerun.io/docs/python/stable/common/ \
    -o docs/external/rerun \
    --max-depth 2
```

### Gymnasium Docs

```bash
uv run python scripts/scrape_docs.py \
    https://gymnasium.farama.org/api/env/ \
    -o docs/external/gymnasium \
    --max-depth 2
```

### Stable-Baselines3 Docs

```bash
uv run python scripts/scrape_docs.py \
    https://stable-baselines3.readthedocs.io/en/master/ \
    -o docs/external/sb3 \
    --max-depth 2 \
    --exclude "/_sources/" \
    --exclude "/genindex"
```

## CLI Reference

```
scrape_docs.py <url> [options]

Arguments:
  url                   Base URL to start scraping from

Options:
  -o, --output PATH     Output directory (default: docs/external)
  --max-depth N         Maximum crawl depth (default: 3)
  --delay SECONDS       Delay between requests (default: 0.5)
  --dry-run             Show what would be scraped without scraping
  --include PATTERN     Regex for URLs to include (repeatable)
  --exclude PATTERN     Regex for URLs to exclude (repeatable)
```

## Output Structure

After scraping, the output directory contains:

```
docs/external/<name>/
├── _index.md           # Navigation index with links
├── _manifest.json      # Machine-readable manifest
├── index.md            # Main page
├── page_name.md        # Individual pages
└── ...
```

Each markdown file includes YAML frontmatter:

```yaml
---
source: https://example.com/docs/page
title: Page Title
---
```

## Agent Usage

When you need to reference external library documentation:

1. **Check if docs exist**: Look in `docs/external/` for the library
2. **Scrape if missing**: Use the CLI to pull docs
3. **Read the index**: Start with `_index.md` to find relevant pages
4. **Reference specific pages**: Read individual `.md` files as needed

### Reading Scraped Docs

```python
# In your agent workflow:
# 1. Check _index.md for available pages
# 2. Read specific pages for API details
# 3. Use the source URL in frontmatter to link back
```

## Tips

### Depth Limits

- `--max-depth 1`: Just the starting page and direct links
- `--max-depth 2`: Good for API references (recommended)
- `--max-depth 3`: Full documentation sections

### Filtering

Use `--include` and `--exclude` with regex patterns:

```bash
# Only include API pages
--include "/api/"

# Exclude source code and search
--exclude "/_sources/" --exclude "/search"
```

### Rate Limiting

The default 0.5s delay is polite. Increase for slower servers:

```bash
--delay 1.0
```

## Maintenance

Scraped docs become stale. Re-run the scraper periodically:

```bash
# Re-scrape with same options (overwrites existing)
uv run python scripts/scrape_docs.py <URL> -o docs/external/<name>
```

Check `_manifest.json` for the `scraped_at` timestamp to see when docs were last updated.

## Troubleshooting

### No content extracted

Some sites use heavy JavaScript rendering. The scraper works best with:
- Static HTML sites
- MkDocs / Sphinx / ReadTheDocs
- GitHub Pages documentation

For JS-heavy sites, consider using a browser-based scraper or the site's API.

### Missing dependencies

```bash
uv pip install requests beautifulsoup4 lxml
```

### Rate limited

Increase delay: `--delay 2.0`

### Too many pages

Reduce depth or add exclude patterns:

```bash
--max-depth 1 --exclude "/changelog" --exclude "/blog"
```
