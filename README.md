# Slop Cop 🚓

Catch and remove AI slop from prose, UI/design, and code, before it reaches a human.

Slop is work that's technically fine and completely forgettable: the machine's default register. It reads smooth, says little, and could have come from anyone or no one. Slop Cop patrols three beats and issues a fix, not just a ticket.

## The one law

**Replace the vague claim with a specific, checkable thing.** Under almost every fix here is the same move: name the number, the person, the date, the mechanism, the actual component. If you strip a slop phrase and have nothing concrete to put in its place, that sentence had nothing to say, cut it.

## Three beats

- **Prose**, cadence uniformity (the #1 tell as of 2026), filler openers, overused verbs/adjectives, Latinate bias, hedging, formulaic structure, vague claims of importance, dramatic headings, hallucinated markup artifacts (`oaicite`, `turn0search0`), and the em dash (now a weaker, dated signal, density over presence).
- **Design**, the cluster of untouched defaults: the indigo-to-violet gradient, Inter everywhere, the fits-anyone hero headline, three equal cards, purposeless motion, plastic AI imagery, no real proof, buzzword soup, emoji bullets, boilerplate meta.
- **Code**, happy-path-only code with no config/logging/edge cases, over-documentation of the obvious, ceremonial over-long names, sterilized over-modular structure, dead/unused imports, duplication, plus vague names and abstractions that don't earn their keep.

It routes automatically based on what you're delivering, and loads only the beat it needs.

## What makes it not over-police

A word on the banned list isn't automatically a crime. Slop Cop respects exclusion zones (quotes, proper names, code examples), lowers severity when a word is anchored to a specific entity or date, and distinguishes literal uses ("Beethoven's symphony") from metaphorical slop ("a symphony of features"). The goal is human, not sterile.

## Install

**Claude Code / Cowork:** add this folder as a skill, or install the `.skill` file.

**Claude Projects:** upload `SKILL.md` and the `references/` folder to project knowledge.

**Custom instructions / API:** paste the core rules from `SKILL.md` into your system prompt; the reference files load on demand.

## Usage

It triggers on its own before delivering drafted prose, a landing page, a component, or code. You can also call it directly: "run Slop Cop on this," "de-slop this post," "grade this draft," "does this sound like ChatGPT?"

Ask it to grade and it returns a score out of 50 across Directness, Specificity, Rhythm, Voice, and Density. Below 35: revise.

## Credits

Synthesized and de-conflicted from a set of excellent open-source anti-slop projects: stop-slop (Hardik Pandya), slopless (seochecks.ai), hallmark (Nutlope), taste-skill (Leonxlnx), desloppify (Peter O'Malley), and the Rossmann Group no-AI-slop writing rules. The design and code beats were hardened with current research on generated-UI tells (the 50ms credibility judgment, the indigo-gradient / Inter cluster) and LLM code smells (happy-path scope, over-documentation, higher smell density on complex tasks), and the prose beat was updated for the 2026 landscape where the em dash is a fading tell and cadence uniformity is the strongest signal. It adds a false-positive-prevention layer so it tickets slop, not vocabulary.

## License

MIT.
