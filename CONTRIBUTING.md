# Contributing Guidelines

Personal guidelines for adding utilities to this repository.

## When to Add a Utility

Add a script here when:
- **Actively using it** - You've used it at least twice in real work
- **Reasonably general** - Could be useful in future projects, not hyper-specific to one dataset
- **Self-contained** - Doesn't require complex setup or project-specific configuration

Don't add:
- One-off scripts for a specific analysis
- Scripts that are tightly coupled to a specific project's structure
- Incomplete or untested code

## Directory Structure

Each utility gets its own directory:

```
utility_name/
├── README.md           # Required: documentation
├── utility_name.py     # The main script (or meaningful name)
├── requirements.txt    # Only if there are dependencies beyond stdlib
└── test/
    ├── input.txt           # Sample input data
    ├── expected_output.txt # Expected output for comparison
    └── run_test.sh         # Test runner script
```

Copy from `template_utility/` when creating a new utility.

## Naming Conventions

- **Directories:** lowercase with underscores, descriptive
  - Good: `gff_to_bed`, `filter_fastq_by_quality`, `extract_fasta_regions`
  - Bad: `converter`, `script1`, `myTool`

- **Scripts:** Match the directory name or be clearly descriptive
  - `gff_to_bed/gff_to_bed.py`
  - `filter_fastq_by_quality/filter_fastq.py`

## Documentation Requirements

Before committing, the README.md must include:

1. **Purpose** - One paragraph explaining what it does and when to use it
2. **Usage** - Working command-line example
3. **Input/Output** - What format goes in, what comes out

Optional but helpful:
- Example input/output snippets
- Edge cases or limitations
- Related utilities

## Code Standards

- Include a docstring at the top of the script
- Use argparse with `--help` documentation
- Validate inputs and provide clear error messages
- Write to stdout by default (allows piping)
- Use `if __name__ == "__main__":` pattern

## Before Committing

- [ ] `bash test/run_test.sh` passes
- [ ] `--help` produces useful output
- [ ] README.md has Purpose, Usage, and Input/Output sections
- [ ] Directory and script names are descriptive
