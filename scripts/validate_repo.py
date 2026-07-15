#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "slop-cop"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_METADATA = SKILL_DIR / "agents" / "openai.yaml"
EXPECTED_NAME = "slop-cop"

errors: list[str] = []

if (ROOT / "SKILL.md").exists():
    errors.append(
        "root-level SKILL.md must not exist; use skills/slop-cop/SKILL.md"
    )

if not SKILL.exists():
    errors.append("missing skills/slop-cop/SKILL.md")
else:
    text = SKILL.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")

    parts = text.split("---", 2)

    if len(parts) < 3:
        errors.append("SKILL.md frontmatter is not closed")
    else:
        frontmatter = parts[1]

        name_match = re.search(
            r"(?m)^name:\s*([^\n#]+)",
            frontmatter,
        )

        if not name_match:
            errors.append("frontmatter is missing name")
        else:
            declared_name = (
                name_match.group(1)
                .strip()
                .strip("\"'")
            )

            if declared_name != EXPECTED_NAME:
                errors.append(
                    "frontmatter name must be "
                    f"{EXPECTED_NAME!r}, found {declared_name!r}"
                )

        if not re.search(
            r"(?m)^description:\s*(?:[>|]-?|\S.+)$",
            frontmatter,
        ):
            errors.append("frontmatter is missing description")

    if len(text.splitlines()) > 500:
        errors.append(
            "SKILL.md exceeds 500 lines; move detail to references"
        )

    reference_paths = set(
        re.findall(
            r"\((references/[^)#?\s]+)",
            text,
        )
    )

    reference_paths.update(
        re.findall(
            r"`(references/[^`]+)`",
            text,
        )
    )

    for relative_path in sorted(reference_paths):
        if not (SKILL_DIR / relative_path).is_file():
            errors.append(
                f"missing referenced file: {relative_path}"
            )

if not OPENAI_METADATA.exists():
    errors.append("missing skills/slop-cop/agents/openai.yaml")
else:
    metadata = OPENAI_METADATA.read_text(encoding="utf-8")

    icon_paths = re.findall(
        r'(?m)^\s*icon_(?:small|large):\s*'
        r'["\']?([^"\'\n]+)["\']?\s*$',
        metadata,
    )

    for relative_path in icon_paths:
        icon = SKILL_DIR / relative_path.strip()

        if not icon.is_file():
            errors.append(
                f"missing OpenAI metadata asset: {relative_path}"
            )

for old_path in (
    ROOT / "references",
    ROOT / "agents",
    ROOT / "assets",
):
    if old_path.exists():
        errors.append(
            f"old root-level path still exists: "
            f"{old_path.relative_to(ROOT)}"
        )

for workflow in (ROOT / ".github" / "workflows").glob("*.y*ml"):
    workflow_text = workflow.read_text(encoding="utf-8")

    if re.search(
        r"(?m)^\s*pull_request_target\s*:",
        workflow_text,
    ):
        errors.append(
            "unsafe trigger pull_request_target in "
            f"{workflow.relative_to(ROOT)}"
        )

if errors:
    for error in errors:
        print(f"ERROR: {error}")

    sys.exit(1)

print("Repository structure and skill references look valid.")
