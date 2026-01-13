#!/bin/bash
# Simple test to verify the utility works as expected
# Run from the utility's root directory: bash test/run_test.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UTILITY_DIR="$(dirname "$SCRIPT_DIR")"

echo "Running test..."

# Run the utility and capture output
python "$UTILITY_DIR/template_script.py" "$SCRIPT_DIR/input.txt" > "$SCRIPT_DIR/actual_output.txt"

# Compare with expected output
if diff -q "$SCRIPT_DIR/expected_output.txt" "$SCRIPT_DIR/actual_output.txt" > /dev/null; then
    echo "PASSED: Output matches expected"
    rm "$SCRIPT_DIR/actual_output.txt"
    exit 0
else
    echo "FAILED: Output differs from expected"
    echo "--- Expected ---"
    cat "$SCRIPT_DIR/expected_output.txt"
    echo "--- Actual ---"
    cat "$SCRIPT_DIR/actual_output.txt"
    rm "$SCRIPT_DIR/actual_output.txt"
    exit 1
fi
