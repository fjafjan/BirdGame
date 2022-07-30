"""
Test calculation of foodcosts
"""

from Card import Food, FoodCost

import pytest

@pytest.fixture
def simple_cost():
    """A simple cost of two fish"""
    return FoodCost([Food.FISH, Food.FISH])

@pytest.fixture
def mixed_cost():
    """A simple cost of one grain and one fruit"""
    return FoodCost([Food.GRAIN, Food.FRUIT])

@pytest.fixture
def simple_wildcard_cost():
    """A cost of one ANY cost"""
    return FoodCost([Food.ANY])

@pytest.fixture
def mixed_wildcard_cost():
    """A mixed wildcard and other cost"""
    return FoodCost([Food.ANY, Food.FRUIT, Food.INVETEBRATE])

def test_insufficient_foodcost(simple_cost):
    """Test the Foodcost class and if we can afford things as expected"""
    insufficient_food = [Food.FISH, Food.GRAIN]
    assert not simple_cost.within_budget(insufficient_food)

def test_sufficient_foodcost(simple_cost):
    """Validate that a simple sufficient foodcost is seen as affordable"""
    sufficent_food = [Food.FISH, Food.INVETEBRATE, Food.FISH]
    assert simple_cost.within_budget(sufficent_food)

def test_replacement_foodcost(simple_cost):
    """Validate that we correct show that we can use any two food as replacement"""
    available_replacement = [Food.INVETEBRATE, Food.INVETEBRATE, Food.INVETEBRATE, Food.INVETEBRATE]
    assert simple_cost.within_budget(available_replacement)

def test_insufficient_replacement_foodcost(simple_cost):
    """Validate that we correct show that we can use any two food as replacement"""
    available_replacement = [Food.GRAIN, Food.INVETEBRATE, Food.INVETEBRATE]
    assert not simple_cost.within_budget(available_replacement)

def test_sufficient_wildcast_foodcost(mixed_wildcard_cost):
    """Validate that wildcards work as intended"""
    sufficient_food = [Food.FRUIT, Food.GRAIN, Food.INVETEBRATE]
    assert mixed_wildcard_cost.within_budget(sufficient_food)

def test_insufficient_wildcast_foodcost(mixed_wildcard_cost):
    """Validate that wildcards work as intended"""
    sufficient_food = [Food.FRUIT, Food.FRUIT, Food.FRUIT]
    assert not mixed_wildcard_cost.within_budget(sufficient_food)

