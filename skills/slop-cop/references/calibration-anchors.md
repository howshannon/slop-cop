# Deterministic calibration anchors

Scores follow fixed penalties rather than holistic impressions:

- Blocker: −30
- Major: −15
- Minor: −5
- Note: −1
- Floor: 0

Count one observable problem once at the highest applicable severity. Similar
wording in separate locations may be one repeated-pattern major rather than
several local minors. Distinct problems receive distinct deductions.

## Anchors

| Findings | Math | Score | Grade | Typical action |
|---|---|---:|---|---|
| None | 100 | 100 | A+ | Ship |
| 2 notes | 100 − 2 | 98 | A+ | Ship |
| 1 minor | 100 − 5 | 95 | A | Tweak |
| 1 major | 100 − 15 | 85 | B | Tweak |
| 1 major + 2 minors | 100 − 15 − 10 | 75 | C | Revise |
| 2 majors + 2 minors | 100 − 30 − 10 | 60 | D- | Rewrite sections |
| 1 blocker + 1 major + 2 minors | 100 − 30 − 15 − 10 | 45 | F | Start over from facts |
| 4 blockers | max(0, 100 − 120) | 0 | F | Start over |

Specificity does not grant bonus points. It may prevent a violation, but it
does not offset a separate repeated structure, unsupported claim, or failure
mode. Preserve strong details while fixing only the cited violations.
