"""Utility classes for performing random toss operations."""

from __future__ import annotations

import random
from typing import List, Sequence, Type


class Tosser:
    """Randomly select sides from a castable object."""

    def __init__(self, castee: Type):
        """Create a new ``Tosser`` for the given object.

        The ``castee`` must expose a ``SIDES`` sequence.
        """

        self.castee = castee

    def toss(self, ntoss: int = 1, unique: bool = False) -> List:
        """Return ``ntoss`` results from ``castee``.

        Parameters
        ----------
        ntoss:
            Number of tosses to perform.
        unique:
            If ``True`` return unique results and ignore any extra requests.
        """

        sides: Sequence = self.castee.SIDES
        if unique:
            return (
                list(sides) if ntoss > len(sides) else random.sample(list(sides), ntoss)
            )

        return [random.choice(list(sides)) for _ in range(ntoss)]
