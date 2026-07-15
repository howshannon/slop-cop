# Code Beat: slop in the codebase

Same law: kill the generic default, force a specific choice. AI-generated code compiles and runs and is often quietly wrong in the same ways, too clean on the surface, missing the real-world substance underneath. Studies find LLM output carries markedly more code smells than human reference solutions, and the gap widens on complex and object-oriented tasks.

Two framings matter before the checklist:

- **Clean is not the problem; generic is.** The tell isn't that AI code is messy, it's that it's a textbook-perfect solution to a toy version of the problem, missing the context and edge cases production demands. The fix is to *add* substance (config, errors, edge cases, real integration), not to make the code sloppier or strip its structure.
- **Both directions of a dial are tells.** AI over-names *and* under-names, over-documents *and* over-abstracts. Right-size, don't just swing the other way.

Use this when reviewing or cleaning code a human will maintain. Two layers: mechanical (objective) and review (judgment).

## Mechanical layer (detectable)

Catch these first, they're objective and often automatable with existing linters (ruff, eslint, bandit, jscpd, import-linter, etc.). Prefer running the real tool over eyeballing.

- **Dead code.** Unused functions, variables, imports, unreachable branches, commented-out blocks left "just in case." Delete them; version control remembers.
- **Unused / speculative imports.** AI imports every package that *might* be useful. Drop what isn't used.
- **Duplication.** The same logic copy-pasted across files (the "stitched from ten Stack Overflow answers" pattern). Extract once, name it well, reuse.
- **Complexity.** Functions doing five things, deep nesting, long parameter lists, high cyclomatic complexity. Split by responsibility.
- **Passthrough wrappers.** Functions that only forward to another with no added value. Inline them.
- **Config bags.** Giant options objects threaded everywhere instead of explicit parameters.
- **Over-defensive noise.** try/except (or try/catch) that swallows everything, null checks on things that can't be null, returns of `None`/`null`/`undefined` where a real value or a raised error belongs.
- **Inconsistent naming within a file.** Regenerating a function repeatedly produces naming soup (`userId`, `user_id`, `uid` in one module). Pick one convention and hold it.

## AI-specific tells (the ones generic review misses)

These come straight from how models write. They're the difference between "clean" and "actually maintainable."

- **Over-documentation of the obvious.** A full docstring on `add(a, b)` explaining that it adds two numbers. Uniform, textbook comments on every trivial helper mean the code reads like a tutorial, not a project. Keep comments that explain *why*; cut the ones that restate *what*.
- **Verbose ceremonial names.** `total_sum_of_numeric_values_in_list` for a one-line helper. AI overshoots readability into legal-contract territory. Names should be specific *and* short enough to scan, `total`, not a sentence.
- **Sterilized structure.** Suspiciously perfect: every function 3–5 lines, single-responsibility to a fault, over-modularized into tiny LEGO bricks, no seams where real logic lives. Real code has some functions that legitimately do more. Don't fragment logic just to hit a line count.
- **Happy-path only, no environment.** The dead giveaway. AI code runs on a desert island: no config or `.env`, no auth token, no logging, no retries, no rate limiting, no timeout handling, no CLI/pipeline integration. It assumes a stable API and perfectly formed input. Add the real-world messiness the model skipped.
- **Missing edge cases.** Empty input, malformed data, nulls, boundary values, concurrent access, partial failure. LLM code assumes the happy path; production doesn't. Name the cases and handle them.
- **Toy-problem scope.** "Clean this CSV" yields a neat loop with no schema validation, no logging of skipped rows, no column handling, no malformed-data path. Solve the real problem, not the tutorial version.

## Review layer (judgment)

The scanner can't see these, reason about intent.

- **Naming.** Does the name say what the thing does, or is it `data`, `handler`, `processItem`, `utils`, `helper` (too vague) or a whole sentence (too verbose)? Aim for specific and scannable.
- **Abstractions.** Does this layer earn its keep, or is it indirection for its own sake? AI loves to wrap. Prefer the concrete until duplication actually demands the abstraction.
- **Module boundaries.** Do the seams follow the domain, or did files get split by mechanical size? Related things together, unrelated things apart.
- **Comments.** Do they explain *why*, or narrate *what* the code already says? Delete narration; keep the reasoning that isn't obvious.
- **Error handling.** Are failures surfaced with context, or silently swallowed? Name what failed and why.

## The fix loop

Don't fix everything at once. Detect, prioritize by impact (correctness and real-world robustness over style), then work highest-impact first. Fix things properly, not minimally, a rename that's still vague, or a split that leaves the same tangle, isn't a fix. And when the fix is "add what's missing" (edge cases, config, error handling), that's usually higher value than cosmetic cleanup.

## Self-check before returning code

1. Any dead code, unused/speculative imports, or commented-out blocks? Remove.
2. Any logic duplicated across files? Extract and name it.
3. Any function doing more than one clear thing, or fragmented into pointless tiny pieces? Right-size it.
4. Any name that's vague (`data`/`handler`) or a full sentence? Make it specific and scannable.
5. Any docstring or comment that restates the obvious? Cut it. Any *why* that's missing? Add it.
6. Does it handle the real world: config/secrets, logging, timeouts, retries, malformed input, edge cases? If not, add them.
7. Does error handling surface context, or swallow it?
8. Is the naming convention consistent across the file?

## Note

The prose and design beats are self-contained. The code beat pairs well with a real linter for the mechanical layer, treat this file as the judgment checklist that sits on top of the tooling, not a replacement for it.
