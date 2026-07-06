#!/usr/bin/env python3
"""
validate-prompts.py

Checks every prompt file under /prompts follows the required template structure:
- Has a top-level H1 title
- Contains required section headers: Role, Context, Task, Constraints, Output Format

Usage:
    python3 scripts/validate-prompts.py
"""

import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Role",
    "## Context",
    "## Task",
    "## Constraints",
    "## Output Format",
]

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def validate_file(filepath: Path) -> list:
    errors = []
    text = filepath.read_text(encoding="utf-8")

    if not text.startswith("# "):
        errors.append("Missing top-level H1 title as the first line")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing required section: '{section}'")

    return errors


def main():
    if not PROMPTS_DIR.exists():
        print(f"ERROR: prompts directory not found at {PROMPTS_DIR}")
        sys.exit(1)

    md_files = sorted(PROMPTS_DIR.rglob("*.md"))
    if not md_files:
        print("No prompt files found.")
        sys.exit(0)

    total_errors = 0
    for filepath in md_files:
        errors = validate_file(filepath)
        if errors:
            total_errors += len(errors)
            rel = filepath.relative_to(PROMPTS_DIR.parent)
            print(f"\n{rel}")
            for e in errors:
                print(f"  - {e}")

    print(f"\nChecked {len(md_files)} prompt file(s).")
    if total_errors:
        print(f"FAILED with {total_errors} issue(s).")
        sys.exit(1)
    else:
        print("All prompt files passed validation.")
        sys.exit(0)


if __name__ == "__main__":
    main()
