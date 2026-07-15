# Benchmark

`cases.yml` is a behavioral contract, not an AI detector dataset. For each
change to a rule, run the cases through the skill in audit/grade mode and record
whether the required findings, preservation constraints, verdict, and score
range are satisfied.

The repository validator checks fixture structure. Model-runtime evaluations
remain manual unless your agent platform exposes a deterministic test runner.
Do not present heuristic-script output as an end-to-end skill result.
