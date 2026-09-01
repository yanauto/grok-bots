# Data

Source lists, one JSON array per use case. Add a bot to exactly one of these files. Do not edit `README.md` on the homepage.

Then run `python3 scripts/render_catalog.py` to refresh `catalog/<category>.md` and the homepage counts.

| File | Use case |
| --- | --- |
| [coding-dev.json](coding-dev.json) | Apps, code, PRs, shipping, site audits |
| [content-writing.json](content-writing.json) | Copy, slides, SEO briefs, outreach drafts |
| [x-social.json](x-social.json) | X briefs, growth, posting, account coaching |
| [ops-productivity.json](ops-productivity.json) | Inbox, calendar, CoS, sales ops, support |
| [research-news.json](research-news.json) | Research, papers, news, competitor diffs |
| [shopping-commerce.json](shopping-commerce.json) | Refunds, shopping, selling, subscriptions |
| [home-life.json](home-life.json) | Home, travel, food, personal life door |
| [other.json](other.json) | Bot craft and anything that does not fit above |
