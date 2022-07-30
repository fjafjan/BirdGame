"""
Test for the Card test!
"""

from Card import Food, FoodCost, Card
from Board import Board
from typing import List
import pytest

from GameSetup import init_deck, init_food

@pytest.fixture
def full_deck() -> List[Card]:
    """The entire deck (currently only five cards)"""
    return init_deck().draw_cards(5)

@pytest.fixture
def raven(full_deck) -> Card:
    """Returns the raven as a sample card."""
    print("Full deck is", full_deck)
    return full_deck[1]



def test_laying_valid_eggs(raven: Card):
    assert raven.eggs() == 0
    raven.lay_egg()
    raven.lay_egg()
    assert raven.eggs() == 2
    raven.remove_egg()
    raven.remove_egg()
    assert raven.eggs() == 0

def test_laying_too_many_eggs(raven: Card):
    assert raven.eggs() == 0
    raven.lay_egg()
    raven.lay_egg()
    raven.lay_egg()
    try:
        raven.lay_egg()
        assert False
    except:
        assert True
    assert raven.eggs() == 3
    raven.remove_egg()
    raven.remove_egg()
    raven.remove_egg()
    assert raven.eggs() == 0
