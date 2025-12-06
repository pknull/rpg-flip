---
version: "1.0"
lastUpdated: "2025-12-06"
lifecycle: "active"
stakeholder: "pknull"
changeTrigger: "scope change, major milestone"
validatedBy: "human"
dependencies: []
---

# Project Brief: rpg-flip

## Purpose

Simple utilities for randomly selecting from a predefined list of sides. Useful for coin flips, dice-like selections, and other random choice operations in RPG contexts.

## Core Features

- `Tosser` class for random selection from any object with a `SIDES` attribute
- Support for multiple tosses
- Unique selection mode (no duplicates)
- Pre-built casts (e.g., Coin)

## Usage

```python
from flipper import Coin, Tosser

t = Tosser(Coin)
print(t.toss())              # e.g. ['Heads']
print(t.toss(ntoss=2))       # Multiple tosses
print(t.toss(ntoss=2, unique=True))  # No duplicates
```

## Technical Stack

- Language: Python
- Testing: pytest
- Installation: pip install -e .
- Runtime dependencies: None

## Success Criteria

- Simple, clean API
- Extensible to any "sided" object
- Well-tested
