from yahtzee import *
import pytest

def test_roll_dice():
    dice = roll_dice()
    assert len(dice) == 5
    for die in dice:
        assert 1 <= die <= 6

def test_is_yahtzee():
    assert is_yahtzee([6,6,6,6,6]) is True 
