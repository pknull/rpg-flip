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
