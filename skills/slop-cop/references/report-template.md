# Report template

## Findings

| Severity | Evidence/location | Observable pattern | Why it matters | Recommended change |
|---|---|---|---|---|

For prose, also tally repeated devices. For design and code, tally the
corresponding observable failures. Count each violation once at its highest
severity.

## Required report-card ticket

```text
🚨 SLOP COP REPORT CARD
To: <recipient or artifact>
Score: <0–100>/100 (<A+ through F>)
Scale: 0 = total slop · 100 = damn, you're not a robot?
Charge: <biggest offense or no citation-worthy violations found>
Evidence: <quoted or observable evidence>
Violations: <n> blocker · <n> major · <n> minor · <n> note
Score math: 100 - (<n>×30 blocker) - (<n>×15 major) - (<n>×5 minor) - (<n>×1 note) = <score>
Citation: <deterministically selected fixed slogan>
Recommended next step: <fixed score-band action>
Fix: <single highest-leverage change>
```

The ticket is required in Audit, Grade, Rewrite, and Ticket modes. For a clean
result, use zero violation counts and explain the evidence for the 100/A+
score.
