#!/usr/bin/env python3
"""Build a deterministic Slop Cop report-card ticket."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PENALTIES = {"blocker": 30, "major": 15, "minor": 5, "note": 1}
SLOGAN_FILE = Path(__file__).resolve().parent.parent / "references" / "ticket-slogans.json"


def score(blockers: int, majors: int, minors: int, notes: int) -> int:
    deduction = (
        blockers * PENALTIES["blocker"]
        + majors * PENALTIES["major"]
        + minors * PENALTIES["minor"]
        + notes * PENALTIES["note"]
    )
    return max(0, 100 - deduction)


def letter_grade(value: int) -> str:
    bands = (
        (97, "A+"), (93, "A"), (90, "A-"), (87, "B+"), (83, "B"),
        (80, "B-"), (77, "C+"), (73, "C"), (70, "C-"), (67, "D+"),
        (63, "D"), (60, "D-"), (0, "F"),
    )
    return next(grade for floor, grade in bands if value >= floor)


def next_step(value: int) -> str:
    if value >= 97:
        return "Ship it. No material revision is required."
    if value >= 90:
        return "Tweak the optional notes, then ship."
    if value >= 80:
        return "Tweak the minor violations before publishing."
    if value >= 77:
        return "Revise the highest-impact violation, then re-score."
    if value >= 70:
        return "Revise the material violations before publishing."
    if value >= 60:
        return "Rewrite the affected sections around concrete facts and structure."
    return "Start over from the strongest factual core; preserve only verified details."


def load_slogans() -> dict[str, list[str]]:
    with SLOGAN_FILE.open(encoding="utf-8") as handle:
        slogans = json.load(handle)
    if set(slogans) != {"bad", "good"} or any(len(slogans[key]) != 30 for key in slogans):
        raise ValueError("ticket-slogans.json must contain exactly 30 bad and 30 good slogans")
    return slogans


def slogan(value: int, blockers: int, majors: int, minors: int, notes: int) -> str:
    bank = load_slogans()["good" if value >= 77 else "bad"]
    index = (value + blockers * 11 + majors * 7 + minors * 3 + notes) % len(bank)
    return bank[index]


def score_math(blockers: int, majors: int, minors: int, notes: int, value: int) -> str:
    return (
        f"100 - ({blockers}×30 blocker) - ({majors}×15 major) "
        f"- ({minors}×5 minor) - ({notes}×1 note) = {value}"
    )


def nonnegative(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("violation counts cannot be negative")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a deterministic Slop Cop report card.")
    parser.add_argument("--recipient", required=True)
    parser.add_argument("--offense", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--fix", required=True)
    parser.add_argument("--blockers", type=nonnegative, default=0)
    parser.add_argument("--majors", type=nonnegative, default=0)
    parser.add_argument("--minors", type=nonnegative, default=0)
    parser.add_argument("--notes", type=nonnegative, default=0)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    value = score(args.blockers, args.majors, args.minors, args.notes)
    print("🚨 SLOP COP REPORT CARD")
    print(f"To: {args.recipient}")
    print(f"Score: {value}/100 ({letter_grade(value)})")
    print("Scale: 0 = total slop · 100 = damn, you're not a robot?")
    print(f"Charge: {args.offense}")
    print(f"Evidence: {args.evidence}")
    print(
        "Violations: "
        f"{args.blockers} blocker · {args.majors} major · "
        f"{args.minors} minor · {args.notes} note"
    )
    print(f"Score math: {score_math(args.blockers, args.majors, args.minors, args.notes, value)}")
    print(f"Citation: {slogan(value, args.blockers, args.majors, args.minors, args.notes)}")
    print(f"Recommended next step: {next_step(value)}")
    print(f"Fix: {args.fix}")


if __name__ == "__main__":
    main()
