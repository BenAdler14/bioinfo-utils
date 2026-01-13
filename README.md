# bioinfo-utils

A collection of reusable bioinformatics utility scripts for common tasks in computational biology.

## Purpose

Single-purpose tools for "everyday" bioinformatics tasks:
- Format converters
- Data parsers
- Simple processing scripts

**What belongs here:** Utilities that solve one specific problem and are useful across multiple projects.

**What belongs in bioinfo-workflows:** Multi-step analysis pipelines, project-specific workflows, anything that chains multiple tools together.

**In this repo, my core philosophy is to decouple utility from publication.** I want to make tools and utilities that I find useful available independent of a traditional publication process. 

## Repository Structure

```
bioinfo-utils/
├── utility_name/
│   ├── README.md           # Documentation for this utility
│   ├── utility_script.py   # The utility itself
│   └── requirements.txt    # Dependencies (if any)
├── another_utility/
│   └── ...
└── template_utility/       # Template for creating new utilities
```

Each utility is self-contained in its own directory with its own documentation.

## Usage

### Option 1: Clone the entire repository
```bash
git clone https://github.com/BenAdler14/bioinfo-utils.git
python bioinfo-utils/utility_name/script.py --help
```

### (Preferred) Option 2: Copy a specific utility
Copy just the directory you need into your project or scripts folder.

### Option 3: Reference directly
```bash
python /path/to/bioinfo-utils/utility_name/script.py input.txt > output.txt
```

## Finding Utilities

Browse the directories in this repository. Each utility has a README.md explaining:
- What problem it solves
- Required inputs and expected outputs
- Usage examples

## AI Development

Tools in this repository are often developed in collaboration with [Claude](https://claude.ai) and [Cursor](https://cursor.com). This is a developing concept and code of ethics and is likely to change in the future. As of 2026, all tools are designed, analyzed, vetted and tested by a human.


