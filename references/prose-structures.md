# Prose Structures: the patterns, not just the words

Slop hides in shape as much as vocabulary. Clean words in a formulaic structure still read as machine output. State the point directly and vary the shape.

## Binary contrasts

False drama from a telegraphed reversal. State Y directly; drop the negation.

- "Not because X. Because Y." / "Not X, but Y."
- "[X] isn't the problem. [Y] is."
- "The answer isn't X. It's Y."
- "It feels like X. It's actually Y."
- "It's not this. It's that." / "isn't X, it's Y"
- "stops being X and starts being Y"
- "not just X but also Y"

**Threshold:** more than two contrasting parallelisms in a 500-word block is a high-confidence AI tell. **Fix:** "The problem is Y." "Y matters here."

## Negative listing

Listing what something is *not* before revealing what it *is*, a rhetorical striptease. "Not a X... Not a Y... A Z." State Z. The reader doesn't need the runway.

## Dramatic fragmentation

Sentence fragments for manufactured profundity. "[Noun]. That's it. That's the [thing].", "X. And Y. And Z.", "This unlocks something. [Word]." Write complete sentences and trust the content.

## Rhetorical setups

Announcing insight instead of delivering it. "What if [reframe]?", "Here's what I mean:", "Think about it:", "And that's okay." Make the point; let readers draw the conclusion.

## False agency

Inanimate things doing human verbs, AI loves this because it dodges naming the actor.

- "a complaint becomes a fix" → someone fixed it
- "the decision emerges" → someone decided
- "the culture shifts" → people changed behavior
- "the data tells us" → someone read it and concluded
- "the market rewards" → buyers pay for things

Name the human. If no specific person fits, use "you" to put the reader in the seat.

## Narrator-from-a-distance

Floating above the scene. "Nobody designed this.", "This happens because...", "People tend to...". Put the reader in the room: "You don't sit down one day and decide to..." beats "Nobody designed this."

## Passive voice

Hides the actor and drains energy. "X was created", "It is believed that", "Mistakes were made", "The decision was reached." Find the actor and put them at the front.

## Sentence starters to avoid

Wh- openers become a crutch: sentences starting with What, When, Where, Which, Who, Why, How. "What makes this hard is..." → "The constraint is [specific constraint]." Also: paragraphs starting with "So", sentences starting with "Look,".

## Heading anti-patterns

Headings describe content; they don't tease it. If it could be a thriller chapter or a YouTube thumbnail, rewrite it.

| Pattern | Bad | Good |
|---------|-----|------|
| "The [Concept] Trap" | "The Initialization Trap" | "Import vs. Initialize: metadata risk" |
| "The [Adjective] [Noun]" | "The Hidden Danger" | "Firmware corruption after power loss" |
| "Why [X] [Dramatic Verb] [Y]" | "Why Rebuilding Destroys Everything" | "How forced rebuilds overwrite parity" |
| "[Noun]: The [Adj] [Noun]" | "Encryption: The Hidden Trap" | "AES-256 on the bridge board" |

Self-check: remove "The" from the front of a heading; if it still leans on a dramatic noun pairing, rewrite. A good heading reads like a technical index entry, specific and boring to non-specialists.

## The thought-leader register (the LinkedIn slop stack)

The most common slop in social posts isn't one bad phrase; it's a *register* built by stacking the same few moves until they become the texture of the whole thing. Any one is fine. Three or more and you're reading a template. This is the pattern to judge in aggregate (see "the second law" in SKILL.md), because each line passes on its own.

The recurring moves:

- **Negation-reversal hook:** "Risk didn't just get more complex. It got faster." "This wasn't a strategy problem. It was a courage problem."
- **Fragment stacks for gravitas:** "One room. Off the record. Two days." "No slides. Hands on a keyboard."
- **Antithesis / "not about X, it's about Y":** "It was never about being right. It's about being ready." "You don't leave knowing more about us. You leave seeing the world differently."
- **The everyone-agreed reveal:** "And not one of them said predict. Every one said adapt."
- **Punchline endings:** every paragraph builds to a short, quotable last line. Individually punchy; in bulk, metronomic.
- **The "and it wasn't close" tag** and the **"same thing from a different angle"** connective, tics that signal generated cohesion.
- **Profundity without content:** "the edge was never prediction," "nobody has it all figured out." Sounds deep, names nothing checkable.

**Why it's a tell:** every move is a reversal or a fragment, so the piece has exactly one rhythm, dressed up as variety. Real writing has long, winding, subordinate-clause sentences next to short ones, paragraphs that end quietly, and points stated flat without a flip.

**The fix:** count the moves. Keep the two strongest (usually the real thesis). Rewrite the rest as ordinary declarative sentences, and let at least a few paragraphs end without a punch. Add one genuinely long, breathing sentence. The specificity (real names, numbers, examples) is what you protect; the reversal-cadence is what you cut.

## Structural and statistical tells

Beyond words, AI text is measurably uniform. Human writing is bursty. As of 2026 this is the strongest signal there is: the classic lexical tells (em dashes, "delve") are now partly trained out, but cadence uniformity survives the longest across model rewrites. Two measures do most of the work: **burstiness** (how much sentence length varies) and **perplexity** (how surprising the word choices are). Humans score high on both; AI scores low.

- **Cadence uniformity (the #1 tell):** sentence after sentence landing in the 18–24 word band, paragraph after paragraph, is the clearest current fingerprint of machine text. Break it deliberately.
- **Paragraph uniformity:** if every paragraph in a section is within ~15% of the others in word count, it reads as generated. Vary length by how much each point actually needs. (Exception: lists and tables are uniform by design.)
- **Sentence burstiness:** a 500-word block with no sentence under 8 words and none over 30 lacks human rhythm. Mix short punches with long clause-heavy sentences.
- **Low perplexity:** if every word is the statistically expected next word, the text reads as generated. Reach for the surprising-but-right word, the specific noun, the unexpected verb.
- **"Not just X, but Y":** LLMs produce roughly one of these per paragraph; humans use it occasionally. More than one per paragraph is a high-confidence tell (see Binary contrasts above).
- **Transition density:** if more than ~30% of paragraphs open with a transition word or adverbial clause, it's artificial. Cut connectors.
- **Opening-word repetition:** three or more consecutive paragraphs starting with the same word or pattern signals mechanical generation.
- **Flat segmental entropy:** AI holds one register from intro to conclusion. Human intros are tighter and declarative; bodies are denser; conclusions shift register. Vary pacing across sections.

## Repetitive layouts (structural slop)

Three sections built from an identical template read as machine output even when each fact is true.

- WRONG: three sections all shaped "In [year], [party] did [thing]. This affected [number]. [Party] responded by [action]."
- RIGHT: section one is a two-paragraph narrative with timeline; section two is a two-sentence summary because it's thinly documented; section three opens with the party's justification, then the contradicting evidence.

Vary paragraph count, sentence rhythm, and how each section opens.

## Model-family fingerprints (for reference)

- **GPT-family:** heavy bullet lists, staccato "It's not X. It's Y." contrasts, rhetorical colons ("Here's the thing:", "The bottom line:"), over-numbered steps.
- **Claude-family:** better sentence variation but flat entropy, conciliatory transitions ("That said", "To be fair", "It's worth considering"), poetic words ("nuanced," "complexities"), diplomatic hedging on documented facts.
- **All models:** uniform paragraphs, predictable section order (Background → Details → Impact → Response), citations clustered at paragraph ends, excessive boldface on concepts and product names.
