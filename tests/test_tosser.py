import random
import pytest

from flipper.Casts import Coin
from flipper.Tosser import Tosser


def test_toss_returns_correct_length():
    random.seed(0)
    t = Tosser(Coin)
    result = t.toss(ntoss=3)
    assert len(result) == 3
    assert all(side in Coin.SIDES for side in result)


def test_unique_toss_results():
    random.seed(0)
    t = Tosser(Coin)
    result = t.toss(ntoss=2, unique=True)
    assert len(result) == 2
    assert len(set(result)) == 2


def test_unique_toss_more_than_sides_returns_all_sides():
    t = Tosser(Coin)
    result = t.toss(ntoss=5, unique=True)
    assert set(result) == set(Coin.SIDES)


def test_missing_sides_raises_value_error():
    class NoSides:
        pass

    with pytest.raises(ValueError, match="must have a SIDES attribute"):
        Tosser(NoSides)


def test_empty_sides_raises_value_error():
    class EmptySides:
        SIDES = []

    with pytest.raises(ValueError, match="cannot be empty"):
        Tosser(EmptySides)


def test_ntoss_zero_returns_empty_list():
    t = Tosser(Coin)
    assert t.toss(ntoss=0) == []


def test_negative_ntoss_raises_value_error():
    t = Tosser(Coin)
    with pytest.raises(ValueError, match="ntoss must be non-negative"):
        t.toss(ntoss=-1)
