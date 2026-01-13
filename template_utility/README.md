# [Utility Name]

Brief one-line description of what this utility does.

## Purpose

What problem does this solve? When would you use this tool?

Example: "Converts GFF3 annotation files to BED format, extracting only gene features with their names preserved in the BED name field."

## Requirements

**Dependencies:**
- Python 3.8+
- Additional packages: see `requirements.txt`

**Input format:**
- Describe expected input format
- Note any assumptions (e.g., "assumes sorted by chromosome")
- Mention file size limitations if relevant

## Usage

```bash
python template_script.py input_file.txt --option value > output.txt
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `input_file` | Yes | Description of input |
| `--option` | No | What this option does (default: X) |
| `--output` | No | Output file (default: stdout) |

### Examples

**Basic usage:**
```bash
python template_script.py data.txt
```

**With options:**
```bash
python template_script.py data.txt --option value --output results.txt
```

## Input/Output Format

### Input
```
Example of input format
with actual data structure
```

### Output
```
Example of output format
showing what to expect
```

## Testing

Run the included test to verify the utility works:

```bash
bash test/run_test.sh
```

The test directory contains:
- `input.txt` - Sample input data
- `expected_output.txt` - Expected output for comparison
- `run_test.sh` - Test runner script

## Notes

- Any caveats or edge cases
- Performance considerations for large files
- Related utilities in this repository
