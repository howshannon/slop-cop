#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
MODULE_PATH = ROOT / "skills" / "slop-cop" / "scripts" / "score_ticket.py"
SPEC = importlib.util.spec_from_file_location("score_ticket", MODULE_PATH)
assert SPEC and SPEC.loader
score_ticket = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(score_ticket)

assert score_ticket.score(0, 0, 0, 0) == 100
assert score_ticket.score(4, 0, 0, 0) == 0
assert score_ticket.score(0, 1, 2, 0) == 75

expected_boundaries = {
    100: "A+", 97: "A+", 96: "A", 93: "A", 92: "A-", 90: "A-",
    89: "B+", 87: "B+", 86: "B", 83: "B", 82: "B-", 80: "B-",
    79: "C+", 77: "C+", 76: "C", 73: "C", 72: "C-", 70: "C-",
    69: "D+", 67: "D+", 66: "D", 63: "D", 62: "D-", 60: "D-",
    59: "F", 0: "F",
}
for value, expected in expected_boundaries.items():
    assert score_ticket.letter_grade(value) == expected

slogans = score_ticket.load_slogans()
assert len(slogans["bad"]) == 30
assert len(slogans["good"]) == 30
assert len(set(slogans["bad"])) == 30
assert len(set(slogans["good"])) == 30
assert score_ticket.slogan(75, 0, 1, 2, 0) == score_ticket.slogan(75, 0, 1, 2, 0)
assert score_ticket.slogan(76, 0, 0, 0, 24) in slogans["bad"]
assert score_ticket.slogan(77, 0, 1, 1, 3) in slogans["good"]

print("Deterministic ticket scoring, grades, and 60 fixed slogans validated.")
