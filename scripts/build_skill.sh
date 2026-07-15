\
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/slop-cop.skill"

rm -rf "$ROOT/dist"
mkdir -p "$ROOT/dist"

python3 - "$ROOT" "$OUT" <<'PYZIP'
from pathlib import Path
import sys
import zipfile

root = Path(sys.argv[1])
out = Path(sys.argv[2])
include = [root / "SKILL.md", root / "references", root / "LICENSE"]

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
    for item in include:
        if item.is_file():
            archive.write(item, Path("slop-cop") / item.name)
        elif item.is_dir():
            for path in sorted(item.rglob("*")):
                if path.is_file():
                    archive.write(
                        path,
                        Path("slop-cop") / path.relative_to(root),
                    )

with zipfile.ZipFile(out) as archive:
    assert "slop-cop/SKILL.md" in archive.namelist()
    assert archive.testzip() is None

print(out)
PYZIP
