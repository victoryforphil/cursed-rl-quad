#!/usr/bin/env bash
set -euo pipefail

# Script to launch TensorBoard for SimHops training runs

MODELS_DIR="${MODELS_DIR:-models}"
TENSORBOARD_PORT="${TENSORBOARD_PORT:-6006}"

# If a path is provided, use it; otherwise find the most recent run
if [ $# -gt 0 ]; then
    RUN_DIR="$1"
    if [ ! -d "$RUN_DIR" ]; then
        echo "Error: Directory '$RUN_DIR' does not exist"
        exit 1
    fi
else
    # Find the most recent run directory
    if [ ! -d "$MODELS_DIR" ]; then
        echo "Error: Models directory '$MODELS_DIR' does not exist"
        exit 1
    fi
    
    RUN_DIR=$(find "$MODELS_DIR" -maxdepth 1 -type d -name "run_*" | sort -r | head -1)
    
    if [ -z "$RUN_DIR" ]; then
        echo "Error: No run directories found in '$MODELS_DIR'"
        exit 1
    fi
    
    echo "Using most recent run: $RUN_DIR"
fi

TENSORBOARD_LOG_DIR="$RUN_DIR/tensorboard"

if [ ! -d "$TENSORBOARD_LOG_DIR" ]; then
    echo "Error: TensorBoard log directory '$TENSORBOARD_LOG_DIR' does not exist"
    echo "This run may not have TensorBoard logging enabled or training hasn't started yet."
    exit 1
fi

echo "Launching TensorBoard..."
echo "  Log directory: $TENSORBOARD_LOG_DIR"
echo "  Port: $TENSORBOARD_PORT"
echo "  URL: http://localhost:$TENSORBOARD_PORT"
echo ""

# Launch TensorBoard
uv run tensorboard --logdir="$TENSORBOARD_LOG_DIR" --port="$TENSORBOARD_PORT" --bind_all
