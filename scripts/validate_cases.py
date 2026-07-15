#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(__file__).resolve().parents[1] / "benchmark" / "cases.yml"
text = path.read_text(encoding="utf-8")
required = ["version:", "cases:", "id:", "beat:", "input:", "expected_verdict:"]
missing = [key for key in required if key not in text]
case_count = text.count("  - id:")
if missing or case_count < 5:
    if missing:
        print("ERROR: missing benchmark fields:", ", ".join(missing))
    if case_count < 5:
        print(f"ERROR: expected at least 5 cases, found {case_count}")
    sys.exit(1)
print(f"Benchmark fixture file contains {case_count} cases.")
