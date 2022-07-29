"""
Test starting the game, selecting a hand and performing each action.
"""
from GameSetup import init_actions, init_deck, init_food

import pytest

@pytest.fixture
def starting_board():
    deck = init_deck()
