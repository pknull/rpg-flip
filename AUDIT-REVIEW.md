# rpg-flip Review

## Summary

rpg-flip is a minimal Python library for randomly selecting from predefined lists of "sides" (e.g., coin flips, magic 8-ball). The codebase is small (~50 lines of actual code), clean, and well-structured for its purpose. Overall health is good for a hobby/utility project, though it lacks input validation and has minimal test coverage for edge cases.

## Critical Issues

- [flipper/Tosser.py:31] No validation that `castee.SIDES` exists or is non-empty. Will raise `AttributeError` if object lacks `SIDES`, or `IndexError` if `SIDES` is empty.
- [flipper/Tosser.py:12] Type hint `Type` is overly permissive - accepts any type, not just objects with `SIDES` attribute. No runtime enforcement of the contract.
- [flipper/Casts.py:35-36] Duplicate entry "My sources say no" in EightBall.SIDES (appears on lines 18 and 35), skewing probability distribution.

## Recommendations

- [High] Add input validation to `Tosser.__init__()` to verify `castee` has a non-empty `SIDES` attribute. Consider raising `ValueError` with descriptive message.
- [Medium] Define a Protocol or ABC for castable objects to enforce `SIDES` attribute at type-check time (e.g., `class Castable(Protocol): SIDES: Sequence[Any]`).
- [Medium] Remove duplicate "My sources say no" entry from EightBall or document if intentional weighting.
- [Medium] Add edge case tests: empty SIDES list, missing SIDES attribute, ntoss=0, negative ntoss values.
- [Low] Consider using `secrets.choice()` instead of `random.choice()` if cryptographic randomness ever needed (unlikely for RPG use).
- [Low] Add py.typed marker and improve type hints for better IDE support.
- [Low] setup.py uses deprecated distutils fallback - consider switching to pyproject.toml.

## Scores (1-10)

- Code Quality: 7
- Architecture: 8
- Completeness: 5
- Standards: 6

## Notes

**Good Patterns:**
- Clean separation between data (Casts.py) and logic (Tosser.py)
- Simple, focused API with sensible defaults
- Proper use of `__all__` for public interface
- Deterministic test seeding with `random.seed(0)`

**Concerns:**
- Tests only cover happy paths; no edge case or error condition tests
- `unique=True` with `ntoss > len(sides)` silently returns all sides without warning - could surprise users expecting exactly ntoss results
- No `__repr__` or `__str__` on Tosser for debugging
- Empty tests/__init__.py serves no purpose (though harmless)

**Questions:**
- Is the duplicate 8-ball response intentional for weighted probability?
- Should `toss(unique=True)` raise when ntoss > len(sides) rather than silently cap?
- Any plans for persistent state (e.g., weighted coins, loaded dice)?

**File Inventory:**
```
flipper/
  __init__.py    (7 lines)  - Package exports
  Casts.py       (37 lines) - Data classes with SIDES lists
  Tosser.py      (38 lines) - Core logic
tests/
  test_tosser.py (28 lines) - Basic happy-path tests
setup.py         (19 lines) - Package metadata
README.md        (28 lines) - Usage documentation
```

Total project code: ~130 lines (excluding Asha framework files, Memory/, Work/).
