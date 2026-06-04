#!/usr/bin/env python3
"""
Self-contained Skill Packager
=============================
Validates and packages a skill folder into a distributable .skill file.

This is a standalone version — it has NO external dependencies beyond
PyYAML, so anyone can run it in their own environment without installing
the full skill-creator toolkit.

Usage:
    python package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python package_skill.py personal-voice
    python package_skill.py personal-voice ./dist
"""

import fnmatch
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    print("❌ PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(1)

# Patterns to exclude when packaging.
EXCLUDE_DIRS = {"__pycache__", "node_modules"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store"}
ROOT_EXCLUDE_DIRS = {"evals"}


def should_exclude(rel_path: Path) -> bool:
    parts = rel_path.parts
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if len(parts) > 1 and parts[1] in ROOT_EXCLUDE_DIRS:
        return True
    name = rel_path.name
    if name in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(name, pat) for pat in EXCLUDE_GLOBS)


def validate_skill(skill_path: Path):
    """Basic validation: SKILL.md exists, has valid frontmatter, exactly one SKILL.md."""
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False, "SKILL.md not found in the skill folder."

    # Exactly one SKILL.md (claude.ai / Skills API reject multiple on upload).
    skill_md_files = [
        p for p in skill_path.rglob("SKILL.md")
        if not any(part in EXCLUDE_DIRS for part in p.relative_to(skill_path).parts[:-1])
    ]
    if len(skill_md_files) > 1:
        extras = sorted(str(p.relative_to(skill_path)) for p in skill_md_files)
        return False, (
            f"Found {len(skill_md_files)} SKILL.md files; a skill must contain exactly one "
            f"at <folder>/SKILL.md. Extras: {', '.join(extras)}. "
            "Rename supporting docs to non-SKILL.md filenames (e.g. references/<topic>.md)."
        )

    # Validate YAML frontmatter with name + description.
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False, "SKILL.md is missing YAML frontmatter (must start with '---')."
    try:
        _, fm, _ = text.split("---", 2)
        meta = yaml.safe_load(fm)
    except Exception as e:
        return False, f"Could not parse YAML frontmatter: {e}"

    if not isinstance(meta, dict):
        return False, "Frontmatter did not parse to a mapping."
    for key in ("name", "description"):
        if not meta.get(key):
            return False, f"Frontmatter is missing required field: '{key}'."

    name = meta["name"]
    if not isinstance(name, str) or not name.replace("-", "").replace("_", "").isalnum():
        return False, f"'name' should be a slug (letters, numbers, hyphens). Got: {name!r}"

    return True, f"Skill '{name}' is valid."


def package_skill(skill_path, output_dir=None):
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists() or not skill_path.is_dir():
        print(f"❌ Error: not a directory: {skill_path}")
        return None

    print("🔍 Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        return None
    print(f"✅ {message}\n")

    skill_name = skill_path.name
    output_path = Path(output_dir).resolve() if output_dir else Path.cwd()
    output_path.mkdir(parents=True, exist_ok=True)
    skill_filename = output_path / f"{skill_name}.skill"

    try:
        with zipfile.ZipFile(skill_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file_path in sorted(skill_path.rglob("*")):
                if not file_path.is_file():
                    continue
                arcname = file_path.relative_to(skill_path.parent)
                if should_exclude(arcname):
                    print(f"  Skipped: {arcname}")
                    continue
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
        print(f"\n✅ Packaged: {skill_filename}")
        return skill_filename
    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    print(f"📦 Packaging skill: {skill_path}\n")
    result = package_skill(skill_path, output_dir)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
