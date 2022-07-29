"""
Test calculation of foodcosts
"""

from Card import FoodTypes, FoodCost

import pytest

@pytest.fixture
def simple_cost():
    """A simple cost of two fish"""
    return FoodCost([FoodTypes.FISH, FoodTypes.FISH])

@pytest.fixture
def mixed_cost():
    """A simple cost of one grain and one fruit"""
    return FoodCost([FoodTypes.GRAIN, FoodTypes.FRUIT])

@pytest.fixture
def simple_wildcard_cost():
    """A cost of one ANY cost"""
    return FoodCost([FoodTypes.ANY])

@pytest.fixture
def mixed_wildcard_cost():
    """A mixed wildcard and other cost"""
    return FoodCost([FoodTypes.ANY, FoodTypes.FRUIT, FoodTypes.INVETEBRATE])

def test_insufficient_foodcost(simple_cost):
    """Test the Foodcost class and if we can afford things as expected"""
    insufficient_food = [FoodTypes.FISH, FoodTypes.GRAIN]
    assert not simple_cost.within_budget(insufficient_food)

def test_sufficient_foodcost(simple_cost):
    """Validate that a simple sufficient foodcost is seen as affordable"""
    sufficent_food = [FoodTypes.FISH, FoodTypes.INVETEBRATE, FoodTypes.FISH]
    assert simple_cost.within_budget(sufficent_food)

def test_replacement_foodcost(simple_cost):
    """Validate that we correct show that we can use any two food as replacement"""
    available_replacement = [FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE]
    assert simple_cost.within_budget(available_replacement)

def test_insufficient_replacement_foodcost(simple_cost):
    """Validate that we correct show that we can use any two food as replacement"""
    available_replacement = [FoodTypes.GRAIN, FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE]
    assert not simple_cost.within_budget(available_replacement)

def test_sufficient_wildcast_foodcost(mixed_wildcard_cost):
    """Validate that wildcards work as intended"""
    sufficient_food = [FoodTypes.FRUIT, FoodTypes.GRAIN, FoodTypes.INVETEBRATE]
    assert mixed_wildcard_cost.within_budget(sufficient_food)

def test_insufficient_wildcast_foodcost(mixed_wildcard_cost):
    """Validate that wildcards work as intended"""
    sufficient_food = [FoodTypes.FRUIT, FoodTypes.FRUIT, FoodTypes.FRUIT]
    assert not mixed_wildcard_cost.within_budget(sufficient_food)

