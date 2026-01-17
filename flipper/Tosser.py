"""Utility classes for performing random toss operations."""

from __future__ import annotations

import random
from typing import Any, List, Protocol, Sequence, runtime_checkable


@runtime_checkable
class Castable(Protocol):
    """Protocol for objects that can be tossed."""

    SIDES: Sequence[Any]


class Tosser:
    """Randomly select sides from a castable object."""

    def __init__(self, castee: type[Castable]):
        """Create a new ``Tosser`` for the given object.

        The ``castee`` must expose a ``SIDES`` sequence.

        Raises
        ------
        ValueError
            If castee lacks SIDES attribute or SIDES is empty.
        """
        if not hasattr(castee, "SIDES"):
            raise ValueError(
                f"{castee.__name__ if hasattr(castee, '__name__') else castee} "
                "must have a SIDES attribute"
            )
        if not castee.SIDES:
            raise ValueError(f"{castee.__name__}.SIDES cannot be empty")
        self.castee = castee

    def toss(self, ntoss: int = 1, unique: bool = False) -> List[Any]:
        """Return ``ntoss`` results from ``castee``.

        Parameters
        ----------
        ntoss:
            Number of tosses to perform. Must be non-negative.
        unique:
            If ``True`` return unique results and ignore any extra requests.

        Raises
        ------
        ValueError
            If ntoss is negative.
        """
        if ntoss < 0:
            raise ValueError(f"ntoss must be non-negative, got {ntoss}")
        if ntoss == 0:
            return []
        sides: Sequence[Any] = self.castee.SIDES
        if unique:
            return (
                list(sides) if ntoss > len(sides) else random.sample(list(sides), ntoss)
            )

        return [random.choice(list(sides)) for _ in range(ntoss)]
