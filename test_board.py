from Card import Card, FoodTypes
from GameSetup import init_deck, init_food
from Board import Board

from typing import List
import pytest

@pytest.fixture
def full_deck() -> List[Card]:
    """The entire deck (currently only five cards)"""
    return init_deck().draw_cards(10)

@pytest.fixture
def full_food() -> List[FoodTypes]:
    """A list with all types of food"""
    return init_food()

@pytest.fixture
def single_starting_bird(full_deck) -> List[Card]:
    """Testing choosing one single bird. TODO could make this generic and return different values"""
    return full_deck[0:1]

@pytest.fixture
def single_starting_bird_food(full_food) -> List[FoodTypes]:
    """A sample food from selecting one bird."""
    return full_food[0:4]

@pytest.fixture
def three_starting_birds(full_deck) -> List[Card]:
    """Test choosing three birds and only some will be playable"""
    return full_deck[1:4]

@pytest.fixture
def three_starting_bird_food(full_food) -> List[Card]:
    """Returns possible food choice when having chosen three birds"""
    return full_food[0:2]


def test_picking_one_bird(single_starting_bird, single_starting_bird_food):
    starting_birds = single_starting_bird
    starting_food = single_starting_bird_food
    test_board = Board(starting_birds, starting_food)
    ## Currently the responsibility is a bit weird!!
    ## the board should hold everything imo.
    playable_birds = test_board.playable_birds()
    print("PLayable birds: ", playable_birds)
    assert starting_birds[0] in playable_birds

def test_picking_three_birds(three_starting_birds, three_starting_bird_food):
    test_board = Board(three_starting_birds, three_starting_bird_food)

    print(three_starting_birds[2])
    playable_birds = test_board.playable_birds()
    print("Playable birds", playable_birds)
    assert three_starting_birds[0] not in playable_birds
    assert three_starting_birds[1] not in playable_birds
    assert three_starting_birds[2] in playable_birds

def test_invalid_starting_food_card_combo(single_starting_bird, three_starting_bird_food):
    try:
        Board(single_starting_bird, three_starting_bird_food)
        assert False
    except Exception:
        assert True

