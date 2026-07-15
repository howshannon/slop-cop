#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT/skills/slop-cop"
OUT="$ROOT/dist/slop-cop.skill"

test -f "$SKILL_DIR/SKILL.md"

rm -rf "$ROOT/dist"
mkdir -p "$ROOT/dist"

python3 - "$ROOT" "$SKILL_DIR" "$OUT" <<'PYZIP'
from pathlib import Path
import sys
import zipfile

root = Path(sys.argv[1])
skill_dir = Path(sys.argv[2])
out = Path(sys.argv[3])

with zipfile.ZipFile(
    out,
    "w",
    zipfile.ZIP_DEFLATED,
) as archive:
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file():
            continue

        archive.write(
            path,
            Path("slop-cop") / path.relative_to(skill_dir),
        )

    license_path = root / "LICENSE"

    if (
        license_path.is_file()
        and not (skill_dir / "LICENSE").exists()
    ):
        archive.write(
            license_path,
            Path("slop-cop") / "LICENSE",
        )

with zipfile.ZipFile(out) as archive:
    names = set(archive.namelist())

    assert "slop-cop/SKILL.md" in names
    assert archive.testzip() is None

print(out)
PYZIP
