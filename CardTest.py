"""
Test for the Card test!
"""

from Card import FoodTypes, FoodTypes

def test_foodcost():
    """Test the Foodcost class and if we can afford things as expected"""
    simple_cost = FoodCost([FoodTypes.FISH, FoodTypes.FISH])
    unsufficient_food = [FoodTypes.FISH, FoodTypes.GRAIN]
    assert simple_cost.less_than(unsufficient_food)
    available_fish = [FoodTypes.FISH, FoodTypes.INVETEBRATE, FoodTypes.FISH]
    assert not simple_cost.less_than(available_fish)
    available_replacement = [FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE]
    assert not simple_cost.less_than(available_replacement)
