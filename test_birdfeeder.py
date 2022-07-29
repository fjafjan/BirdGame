from Player import Player
from Types import FoodTypes, BirdFeederDice
from Birdfeeder import BirdFeeder


import pytest

class MockPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
    def choose_grain_or_invertebret(self) -> FoodTypes:
        return FoodTypes.GRAIN


@pytest.fixture
def birdfeeder() -> BirdFeeder:
    ret = BirdFeeder()
    ret._dice = [BirdFeederDice.FISH, BirdFeederDice.FRUIT, BirdFeederDice.FRUIT, BirdFeederDice.GRAIN_OR_INVETEBRET, BirdFeederDice.FISH]
    return ret 

@pytest.fixture
def player() -> MockPlayer:
    return MockPlayer()

# def test_birdfeeder_types(birdfeeder: BirdFeeder):
#     possible_food = birdfeeder.food()
#     print("Possible food is", possible_food)
#     assert FoodTypes.FISH in possible_food
#     assert FoodTypes.FRUIT in possible_food
#     assert FoodTypes.GRAIN in possible_food
#     assert FoodTypes.INVETEBRATE in possible_food
#     assert FoodTypes.RODENT not in possible_food

def reset_birdfeeder(birdfeeder: BirdFeeder):
    """Resets the birdfeeder between tests to pre-defined state."""
    birdfeeder._dice = [BirdFeederDice.FISH, BirdFeederDice.FRUIT, BirdFeederDice.FRUIT, BirdFeederDice.GRAIN_OR_INVETEBRET, BirdFeederDice.FISH]

def test_choose_valid_food(birdfeeder: BirdFeeder, player: MockPlayer):
    """
    Tests gaining some food from the birdfeeder.
    """
    my_food = []
    reset_birdfeeder(birdfeeder)
    my_food.append(birdfeeder.choose_dice(BirdFeederDice.FISH, player))
    my_food.append(birdfeeder.choose_dice(BirdFeederDice.FRUIT, player))
    my_food.append(birdfeeder.choose_dice(BirdFeederDice.FRUIT, player))
    ## We default to choosing grain.
    my_food.append(birdfeeder.choose_dice(BirdFeederDice.GRAIN_OR_INVETEBRET, player))
    assert my_food.count(FoodTypes.FRUIT) == 2
    assert my_food.count(FoodTypes.FISH) == 1
    assert my_food.count(FoodTypes.GRAIN) == 1
    assert my_food.count(FoodTypes.INVETEBRATE) == 0
    assert my_food.count(FoodTypes.RODENT) == 0

def test_choose_invalid_food(birdfeeder: BirdFeeder, player: MockPlayer):
    """
    Test choosing more dice than there are, or types not in the birdfeeder.
    """
    my_food = []
    reset_birdfeeder(birdfeeder)
    my_food.append(birdfeeder.choose_dice(BirdFeederDice.GRAIN_OR_INVETEBRET, player))
    try:
        my_food.append(birdfeeder.choose_dice(BirdFeederDice.GRAIN_OR_INVETEBRET, player))
        assert False
    except:
        assert True
    try:
        my_food.append(birdfeeder.choose_dice(BirdFeederDice.RODENT, player))
        assert False
    except:
        assert True
    assert len(my_food) == 1

def test_dice_outside_birdfeeder(birdfeeder: BirdFeeder, player: MockPlayer):
    """Tests the number of dice outside the birdfeeder"""
    reset_birdfeeder(birdfeeder)
    dice_outside = birdfeeder.roll_dice_not_in_birdfeeder()
    assert len(dice_outside) == 0
    birdfeeder.choose_dice(BirdFeederDice.FISH, player)
    birdfeeder.choose_dice(BirdFeederDice.FRUIT, player)
    dice_outside = birdfeeder.roll_dice_not_in_birdfeeder()
    assert len(dice_outside) == 2
    birdfeeder.reroll()
    dice_outside = birdfeeder.roll_dice_not_in_birdfeeder()
    assert len(dice_outside) == 0

