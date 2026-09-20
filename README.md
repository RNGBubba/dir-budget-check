# dir-budget

A small, dependency-free CLI that fails when a directory's regular files exceed a configured byte budget. It is designed for CI checks on generated artifacts, build outputs, caches, and package contents.

## Usage

```bash
uv run dir-budget ./dist --max-bytes 10485760
```

The command prints a JSON report. Exit codes:

- `0`: total bytes are within the budget
- `1`: total bytes exceed the budget
- `2`: invalid arguments or directory

It recursively counts regular files and ignores symlinks. The budget is inclusive: exactly the limit passes.

## Development

```bash
uv sync
python -m pytest -q
```

The library API is also available:

```python
from dirbudget import measure_directory
report = measure_directory("dist", 10_000_000)
```
