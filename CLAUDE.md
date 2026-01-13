# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Collection of reusable bioinformatics utility scripts. Each utility is self-contained in its own directory with documentation. Primarily Python scripts, occasionally small Snakemake workflows.

## Repository Structure

```
bioinfo-utils/
├── utility_name/           # Each utility in its own directory
│   ├── README.md           # Purpose, usage, input/output format
│   ├── script.py           # The utility
│   ├── requirements.txt    # Dependencies (if any)
│   └── test/               # Test case
│       ├── input.txt
│       ├── expected_output.txt
│       └── run_test.sh
└── template_utility/       # Template for new utilities
```

## Testing

Each utility includes a test case. Run with:
```bash
bash test/run_test.sh
```

## Creating New Utilities

1. Copy `template_utility/` to a new directory with a descriptive name (lowercase, underscores)
2. Modify the template files for your utility
3. Ensure README.md has: Purpose, Usage example, Input/Output format

## Code Conventions

- Scripts use argparse with helpful `--help` output
- Default output to stdout (enables piping)
- Validate inputs with clear error messages
- Use `if __name__ == "__main__":` pattern

## What Belongs Here vs. bioinfo-workflows

- **Here:** Single-purpose utilities (format converters, parsers, simple processors)
- **bioinfo-workflows:** Multi-step pipelines, project-specific analysis workflows
