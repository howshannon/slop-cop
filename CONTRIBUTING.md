# Contributing

1. Create a focused branch and pull request; do not push directly to `main`.
2. Explain the observable failure the rule fixes and include a before/after
   fixture in `benchmark/cases.yml`.
3. Rules must not infer AI authorship from style alone.
4. Do not add unsourced model-version claims or numeric thresholds.
5. Do not add code that executes reviewed content or downloads and runs remote
   code during review.
6. Run `make check` and `make package` before opening the pull request.
7. Keep `skills/slop-cop/SKILL.md` compact; put detailed examples and evidence
   in directly linked reference files.
