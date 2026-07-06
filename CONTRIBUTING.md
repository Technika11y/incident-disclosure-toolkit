# Contributing

## Ground rules

- **Not legal advice — keep it that way.** Rules are representative and must stay clearly labelled
  as such. Every rule cites an authority; new rules must too.
- **Honesty contract:** the README status table matches the code; a capability PR updates it.
- **License:** Apache-2.0. **Sign-off:** `git commit -s`.

## Dev loop

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m disclosure.cli obligations examples/incident.json
```

## Design conventions

- `obligations.py` is **pure** (facts in, obligations out) and deterministic — deadlines come from
  the supplied `discovered_date`, never the clock. That keeps it testable.
- Prefer rules that map to a citable legal/─norm authority over generic advice.
