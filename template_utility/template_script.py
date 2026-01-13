#!/usr/bin/env python3
"""
Brief description of what this script does.

Longer description if needed, explaining the use case and any important
details about the implementation or assumptions.

Example:
    python template_script.py input.txt --column 2 > output.txt
"""

import argparse
import sys
from pathlib import Path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Input file to process"
    )
    parser.add_argument(
        "--column",
        type=int,
        default=1,
        help="Column to extract (1-indexed, default: 1)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file (default: stdout)"
    )
    return parser.parse_args()


def validate_input(input_path: Path) -> None:
    """Validate that input file exists and is readable."""
    if not input_path.exists():
        sys.exit(f"Error: Input file not found: {input_path}")
    if not input_path.is_file():
        sys.exit(f"Error: Not a file: {input_path}")


def process_file(input_path: Path, column: int):
    """
    Process the input file and yield results.

    Args:
        input_path: Path to input file
        column: 1-indexed column number to extract

    Yields:
        Processed lines/records
    """
    col_idx = column - 1  # Convert to 0-indexed

    with open(input_path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            fields = line.split("\t")
            if col_idx >= len(fields):
                print(
                    f"Warning: Line {line_num} has only {len(fields)} columns, "
                    f"skipping (requested column {column})",
                    file=sys.stderr
                )
                continue

            yield fields[col_idx]


def main():
    """Main entry point."""
    args = parse_args()

    validate_input(args.input_file)

    # Set up output
    out_handle = open(args.output, "w") if args.output else sys.stdout

    try:
        for result in process_file(args.input_file, args.column):
            print(result, file=out_handle)
    finally:
        if args.output:
            out_handle.close()


if __name__ == "__main__":
    main()
