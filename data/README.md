# Catalog data

`bots.json` is the source of truth for verified public Grok Bot share links.

Each entry is:

| Field | Meaning |
| --- | --- |
| `name` | Name as shown on the share page |
| `role` | One-line role |
| `url` | Exact `https://x.ai/bot/<id>` share URL |
| `verified` | Date the share page was opened (`YYYY-MM-DD`) |

Deduplicate by `url`. “Verified” means the share page loaded and showed Add to Grok Bot. It is not an endorsement.

Add catalog entries only in `bots.json`. See [CONTRIBUTING.md](../CONTRIBUTING.md).
