---
version: "1.0"
lastUpdated: "2025-12-06"
lifecycle: "active"
stakeholder: "pknull"
changeTrigger: "tool change, convention discovery"
validatedBy: "human"
dependencies: []
---

# Technical Environment: rpg-flip

## Language & Runtime

- **Language**: Python
- **Package Manager**: pip
- **Testing**: pytest
- **Runtime Dependencies**: None

## Project Structure

```
rpg-flip/
├── flipper/           # Main library
├── tests/             # Test suite
├── setup.py           # Package config
├── README.md
├── Memory/            # Asha Memory Bank
└── CLAUDE.md
```

## Installation

```bash
pip install -e .
```

## Testing

```bash
pytest
```

## Key Classes

- `Tosser` - Random selection from sided objects
- `Coin` - Pre-built coin cast (Heads/Tails)
- `Casts` - Collection of example casts
