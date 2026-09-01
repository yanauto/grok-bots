# Contributing

This list only includes Grok Bot share links that someone has opened and confirmed. Do not add a bot from another list, a screenshot, or a URL you have not opened.

## Verification checklist

- [ ] Open the public share URL (`https://x.ai/bot/<id>`) in a browser.
- [ ] Confirm the page loads and shows Add to Grok Bot (not a 404 or a dead link).
- [ ] Record the bot name as shown on the share page.
- [ ] Record the share id from the URL.
- [ ] Write a one-line role (what the share page presents, not a sales pitch).
- [ ] Use today’s date as the verified date (`YYYY-MM-DD`).
- [ ] Do not include secrets, API keys, private prompts, or personal information.
- [ ] Do not claim the bot is official or endorsed by xAI or by this repo.

## Pull request

Add one object to `data/bots.json`. Do not add a row to `README.md`. Deduplicate by `url`. Unverified bots will be rejected.

```json
{
  "name": "Bot name / Author",
  "role": "One-line role from the share page",
  "url": "https://x.ai/bot/<id>",
  "verified": "YYYY-MM-DD"
}
```

Optional: `python3 scripts/render_catalog.py` prints a markdown table to stdout for local review.
