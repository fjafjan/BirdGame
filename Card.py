from enum import Enum
from typing import List, Dict, Set

from Types import *
from FoodCost import FoodCost

class Card:
    """
    Describes a bird card. Each bird card has a unique name, a cost in food,
    a nest type and a list of possible habitats in can live in.
    """
    def __init__(self, 
        name: str, 
        cost: List[FoodTypes], 
        nest: NestTypes, 
        possible_habitats: List[Habitat],
        egg_capacity: int):
        self.name = name
        self.cost = FoodCost(cost)
        self.nest = nest
        self.egg_capacity = egg_capacity
        self.eggs = 0
        self.food = []
        self.cards = []
        if Habitat.ANY in possible_habitats:
            self.possible_habitats = [Habitat.FIELD, Habitat.FOREST, Habitat.OCEAN]
        else:
            self.possible_habitats = possible_habitats

    def lay_egg(self) -> None:
        """
        Lays an egg on this bird. Raises exception if there is no free slot.
        """
        if self.eggs == self.egg_capacity:
            raise Exception("Cannot lay egg, already at full capacity")
        self.eggs += 1

    def has_egg_slot(self) -> bool:
        if self.eggs <= self.egg_capacity:
            return True
        else:
            return False


    def eggs(self) -> int:
        """The number of eggs currently on this bird"""
        return self.eggs

    def cached_food(self) -> List[FoodTypes]:
        """Returns all food cached on this card"""
        return self.cached_food

    def tucked_cards(self) -> List:
        """Returns all cards tucked under this card"""
        return self.tucked_cards

    def __str__(self):
        return f"{self.name}: {self.cost}, {self.nest}, {self.possible_habitats}"


