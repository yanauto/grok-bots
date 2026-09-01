# Contributing

This list only includes Grok Bot share links that someone has opened and confirmed. Do not add a bot from another list, a screenshot, or a URL you have not opened.

This repo is maintained by yanauto. Add bots to the use-case files under `data/`, not to `README.md`.

## Verification checklist

- [ ] Open the public share URL (`https://x.ai/bot/<id>`) in a browser.
- [ ] Confirm the page loads and shows Add to Grok Bot (not a 404 or a dead link).
- [ ] Record the bot name as shown on the share page.
- [ ] Record the author if the share page shows one; otherwise leave `author` as `""`.
- [ ] Record the share id from the URL.
- [ ] Write a one-line role (what the share page presents, not a sales pitch).
- [ ] Use today’s date as the verified date (`YYYY-MM-DD`).
- [ ] Put the object in exactly one use-case file:
  - `data/coding-dev.json`
  - `data/content-writing.json`
  - `data/x-social.json`
  - `data/ops-productivity.json`
  - `data/research-news.json`
  - `data/shopping-commerce.json`
  - `data/home-life.json`
  - `data/other.json`
- [ ] Deduplicate by `url`.
- [ ] Do not include secrets, API keys, private prompts, or personal information.
- [ ] Do not claim the bot is official or endorsed by xAI or by this repo.

## Pull request

Add one object to the matching `data/<category>.json` file. Do not add a row to `README.md`. Then run:

```bash
python3 scripts/render_catalog.py
```

That refreshes `catalog/<category>.md` and the homepage category counts. Unverified bots will be rejected.
