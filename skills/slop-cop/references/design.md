# Design patrol

Review generated interfaces as product design, not as a screenshot-style test.
First identify the user, task, content, brand constraints, platform, and state.
When the brief is missing, state assumptions instead of pretending a generic
SaaS dashboard is correct.

## Blockers

- Fabricated proof: invented customers, testimonials, usage metrics, awards,
  reviews, partner logos, security claims, or compliance badges.
- Dark patterns: disguised ads, forced continuity, obstructed cancellation,
  confirmshaming, hidden costs, misleading scarcity, or consent that is harder
  to refuse than accept.
- Missing access: keyboard traps, unusable focus order, unlabeled controls,
  insufficient contrast, interaction conveyed only by color, or motion with no
  reduced-motion path.
- Unsafe or deceptive controls: destructive actions without confirmation or
  recovery, ambiguous permissions, fake browser/OS chrome, or controls that
  imply functionality that does not exist.

## Common slop patterns

1. **Brief-free defaults.** Purple-blue gradients, generic dashboards, random
   productivity metrics, startup slogans, or testimonial strips inserted when
   the product does not require them.
2. **Container inflation.** Cards inside cards, every control as a pill, huge
   corner radii, excessive shadows, floating glass panels, and bento grids used
   as decoration rather than hierarchy.
3. **Centered-everything composition.** Centered hero, centered body copy,
   centered feature cards, and centered CTA regardless of reading or task flow.
4. **Fake specificity.** Arbitrary charts, avatars, percentages, activity feeds,
   or terminal output that make the mockup look real but misrepresent the
   product.
5. **Template density.** Eyebrow label → giant headline → gradient word → three
   cards → logo wall → testimonials → final CTA, regardless of content.
6. **Ornamental tech.** Glowing grids, circuit traces, chrome robot heads,
   floating code, faux command lines, and hacker imagery that do not explain the
   product.
7. **Redrawn platform chrome.** Fake browser tabs, traffic-light buttons,
   mobile status bars, or editor shells that look interactive but are merely
   decoration.
8. **State blindness.** No loading, empty, error, offline, disabled, success,
   permission, overflow, long-text, mobile, hover, focus, or reduced-motion
   states.
9. **Copy/UI mismatch.** Labels describe aspirations rather than actions;
   buttons say “Get started” when the next step is specific; errors blame the
   user or omit recovery.
10. **Brand flattening.** The interface ignores supplied colors, typography,
    imagery, density, audience, or content voice and replaces them with a
    generic design-system default.

## Review workflow

1. Restate the product objective and primary user task.
2. Inventory information hierarchy and required states.
3. Ticket blockers before aesthetic preferences.
4. Cite the exact component or repeated pattern.
5. Recommend deletions before additions.
6. Verify mobile behavior, keyboard/focus behavior, error recovery, content
   authenticity, and brand fit.

## Report

For each finding give: severity, location/component, observable evidence, why it
hurts the task, and a concrete change. Do not call a design “AI-generated”; call
it generic, misleading, inaccessible, repetitive, or unsupported.
