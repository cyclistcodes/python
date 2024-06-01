from yahtzee import *
import pytest

def test_roll_dice():
    dice = roll_dice()
    assert len(dice) == 5
    for die in dice:
        assert 1 <= die <= 6
