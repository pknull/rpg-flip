# rpg-flip

Simple utilities for randomly selecting from a predefined list of sides. The
package exposes a `Tosser` class that can operate on any object which defines a
`SIDES` attribute. A couple of example casts are provided in `flipper.Casts`.

> This project is partially managed by [Asha](https://github.com/pknull/asha), a Claude Code framework.

## Usage

```python
from flipper import Coin, Tosser

t = Tosser(Coin)
print(t.toss())  # e.g. ['Heads']
print(t.toss(ntoss=2))
print(t.toss(ntoss=2, unique=True))
```

## Development

Install dependencies (none are required for runtime) and run tests with `pytest`:

```bash
pip install -e .
pytest
```
