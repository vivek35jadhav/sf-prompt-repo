# Contributing

Thanks for helping grow this library! A few simple rules keep it useful for everyone.

## Adding a new prompt

1. Pick the right folder under `/prompts` (create a new subfolder only if none of the existing categories fit)
2. Copy `templates/_prompt-template.md` into that folder
3. Name the file in `kebab-case.md`, verb-first where possible:
   - Good: `create-date-range-validation.md`, `generate-batch-class.md`
   - Avoid: `ValidationRule1.md`, `misc-stuff.md`
4. Fill out every section of the template — don't remove headers, even if a section is short
5. If possible, add a sample output to `/examples` in the matching subfolder
6. Open a PR using the PR template

## Editing an existing prompt

- Keep the existing structure/headers intact
- Explain *why* in your PR description, not just *what* changed
- If your change is a significant rewrite, consider whether it should be a new prompt instead (to avoid breaking existing users' workflows)

## Style rules

- Prompts should be **tool-agnostic** — they should work reasonably well in Claude, ChatGPT, or Copilot
- Always include a "Context (fill before use)" section — never hardcode object/field names into the base prompt
- Always ask the AI to flag assumptions and edge cases in its output
- Keep language concise; avoid Salesforce jargon that a mid-level dev wouldn't recognize without explanation

## Requesting a new prompt

If you need a prompt that doesn't exist yet, open an issue using the "New Prompt Request" template instead of a blank issue.

## Code of conduct

Be respectful, be constructive, assume good intent.
