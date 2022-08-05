from typing import List
# pylint: disable=redefined-outer-name
import pytest

from Card import Card, Food
from FoodCost import FoodCost
from GameSetup import init_deck, init_food
from Board import Board
from Types import Habitat, Nest
from Player import Player


@pytest.fixture
def full_deck() -> List[Card]:
    """The entire deck (currently only five cards)"""
    return init_deck().draw_cards(10)

@pytest.fixture
def full_food() -> List[Food]:
    """A list with all types of food"""
    return init_food()

@pytest.fixture
def single_starting_bird(full_deck) -> List[Card]:
    """Testing choosing one single bird. TODO could make this generic and return different values"""
    return full_deck[0:1]

@pytest.fixture
def single_starting_bird_food(full_food) -> List[Food]:
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

@pytest.fixture
def simple_board(single_starting_bird: List[Card], single_starting_bird_food: List[Food]):
    """Return a deck initialized with a single bird and four food."""
    return Board(single_starting_bird, single_starting_bird_food)



@pytest.fixture
def board_with_birds(three_starting_birds: List[Card], three_starting_bird_food: List[Card]):
    """Returns a board with three birds played on it."""
    starting_board = Board(three_starting_birds, three_starting_bird_food)
    starting_board.habitat_slots[Habitat.FOREST].append(three_starting_birds[0])
    starting_board.habitat_slots[Habitat.FIELD].append(three_starting_birds[1])
    starting_board.habitat_slots[Habitat.OCEAN].append(three_starting_birds[2])
    return starting_board

def test_picking_one_bird(single_starting_bird, single_starting_bird_food):
    """
    Try picking one bird and ensure that it is playable
    """
    starting_birds = single_starting_bird
    starting_food = single_starting_bird_food
    test_board = Board(starting_birds, starting_food)

    playable_birds = test_board.playable_birds()
    print("PLayable birds: ", playable_birds)
    assert starting_birds[0] in playable_birds

def test_picking_three_birds(three_starting_birds, three_starting_bird_food):
    """
    Try picking three birds and ensure that only one of these is playable.
    """
    test_board = Board(three_starting_birds, three_starting_bird_food)

    playable_birds = test_board.playable_birds()
    assert three_starting_birds[0] not in playable_birds
    assert three_starting_birds[1] not in playable_birds
    assert three_starting_birds[2] in playable_birds

def test_invalid_starting_food_card_combo(single_starting_bird, three_starting_bird_food):
    try:
        Board(single_starting_bird, three_starting_bird_food)
        assert False
    except ValueError:
        assert True


def test_gain_food(simple_board: Board):
    """
    Test simply gaining some food.
    """
    assert len(simple_board.food_tokens()) == 4
    simple_board.gain_food(Food.FISH)
    simple_board.gain_food(Food.RODENT)
    assert len(simple_board.food_tokens()) == 6

def test_gain_invalid_food(simple_board: Board):
    """
    Test gaining an ANY food to ensure this will raise an exception. Note that this
    will need to be changed if implementing nectar i.e. wildcard food.
    """
    assert len(simple_board.food_tokens()) == 4
    try:
        simple_board.gain_food(Food.ANY)
    except ValueError:
        assert len(simple_board.food_tokens()) == 4

class MockPlayer(Player):
    """Mocked player used to choose what food we want to spend to play the Raven."""
    def choose_food_to_spend(self, available_food: List[Food], cost: FoodCost) -> List[Food]:
        """Hardcoded food to spent."""
        return [Food.GRAIN, Food.INVETEBRATE, Food.RODENT]

def test_play_bird(simple_board: Board):
    """
    Test playing a playable bird, ensuring that the correct price is paid.
    """
    playable_bird = simple_board.playable_birds()
    playable_bird = [bird for bird in playable_bird]
    assert len(playable_bird) == 1
    assert len(simple_board.bird_cards()) == 1
    assert len(simple_board.food_tokens()) == 4
    print(simple_board.food_tokens())
    mock_player = MockPlayer()
    simple_board.play_bird(playable_bird[0], Habitat.FIELD, mock_player)
    assert len(simple_board.playable_birds()) == 0
    assert len(simple_board.bird_cards()) == 0
    assert len(simple_board.food_tokens()) == 1

def test_play_invalid_bird(simple_board: Board):
    """
    Test playing a bird that is not in our hand.
    """
    fake_bird = Card("Fake", [], Nest.ANY, [Habitat.ANY], 9)
    try:
        simple_board.play_bird(fake_bird, Habitat.FOREST, MockPlayer())
    except KeyError:
        assert True

def test_total_eggs(board_with_birds: Board):
    """
    Try laying eggs on different birds and make sure egg count goes up.
    """
    eggable_birds = board_with_birds.eggable_birds()
    assert board_with_birds.total_eggs() == 0
    board_with_birds.lay_egg(eggable_birds[0])
    board_with_birds.lay_egg(eggable_birds[1])
    assert board_with_birds.total_eggs() == 2
    board_with_birds.lay_egg(eggable_birds[1])
    board_with_birds.lay_egg(eggable_birds[2])
    assert board_with_birds.total_eggs() == 4
