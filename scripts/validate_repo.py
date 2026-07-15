\
#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
EXPECTED_NAME = "slop-cop"
errors: list[str] = []

if not SKILL.exists():
    errors.append("missing root-level SKILL.md")
else:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter is not closed")
    else:
        frontmatter = parts[1]
        match = re.search(r"(?m)^name:\s*([^\n#]+)", frontmatter)
        if not match:
            errors.append("frontmatter is missing name")
        else:
            declared = match.group(1).strip().strip("\"'")
            if declared != EXPECTED_NAME:
                errors.append(
                    f"frontmatter name must be {EXPECTED_NAME!r}, found {declared!r}"
                )

        if not re.search(r"(?m)^description:\s*(>|\S)", frontmatter):
            errors.append("frontmatter is missing description")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md exceeds 500 lines; move detail to references")

    for rel in re.findall(r"`(references/[^`]+)`", text):
        if not (ROOT / rel).is_file():
            errors.append(f"missing referenced file: {rel}")

if ROOT.name != EXPECTED_NAME:
    print(
        f"WARNING: local checkout folder is {ROOT.name!r}. "
        f"Install or clone the skill as a folder named {EXPECTED_NAME!r}."
    )

for path in (ROOT / ".github" / "workflows").glob("*.y*ml"):
    workflow = path.read_text(encoding="utf-8")
    if re.search(r"(?m)^\s*pull_request_target\s*:", workflow):
        errors.append(f"unsafe trigger pull_request_target in {path.relative_to(ROOT)}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("Repository structure and skill references look valid.")
