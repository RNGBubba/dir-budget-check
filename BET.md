# dir-budget-check

Offer: a dependency-free CI CLI that measures regular-file bytes recursively and fails when a directory exceeds an inclusive byte budget.

Price: $9 one-time for a packaged CI recipe / customization; the public repository is the free lead magnet.

30-day path: publish the working tool, document GitHub Actions usage, and offer small paid adaptations for build-artifact limits. No paid listing or outreach was performed.

Human click: none required for the shipped artifact. GitHub publication used the already-authenticated RNGBubba account.

Repository: https://github.com/RNGBubba/dir-budget-check

Verification:

- `uv run pytest -q` -> 7 passed
- real CLI over-budget invocation returned exit code 1 and emitted JSON report
- DoneMeans receipt: `receipts/t_bc34d8e19283.json`
- receipt verification command: `uv run --project /home/vboxuser/projects/donemeans donemeans --root /home/vboxuser/projects/overnight-revenue/bets/dir-budget receipt verify receipts/t_bc34d8e19283.json`
- commit: `73deda67e426b211df7e1720ae41e2bbef70d2d9`
