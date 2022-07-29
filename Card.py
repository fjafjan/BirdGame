from enum import Enum
from typing import Callable, List, Dict, Set

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
        egg_capacity: int,
        activation_func: Callable = None):
        self._name = name
        self._cost = FoodCost(cost)
        self._nest = nest
        self._egg_capacity = egg_capacity
        self._eggs = 0
        self._food = []
        self._cards = []
        self._activation_func = activation_func
            
        if Habitat.ANY in possible_habitats:
            self._possible_habitats = [Habitat.FIELD, Habitat.FOREST, Habitat.OCEAN]
        else:
            self._possible_habitats = possible_habitats

    def activate(self):
        """
        Activates this card if there is an activation function.
        TODO Determine what inputs this function will need!
        """
        if self._activation_func is not None:
            self._activation_func()

    def lay_egg(self) -> None:
        """
        Lays an egg on this bird. Raises exception if there is no free slot.
        """
        if self._eggs == self._egg_capacity:
            raise Exception("Cannot lay egg, already at full capacity")
        self._eggs += 1
    
    def remove_egg(self) -> None:
        """
        Removes an egg from this card. Raises an exception if there is no egg to remove
        """
        if self._eggs <= 0:
            raise Exception(f"No eggs to remove from {self}")
        self._eggs -= 1

    def has_egg_slot(self) -> bool:
        if self._eggs <= self.egg_capacity:
            return True
        else:
            return False


    def eggs(self) -> int:
        """The number of eggs currently on this bird"""
        return self._eggs

    def cached_food(self) -> List[FoodTypes]:
        """Returns all food cached on this card"""
        return self._cached_food

    def tucked_cards(self) -> List:
        """Returns all cards tucked under this card"""
        return self._tucked_cards

    def __str__(self):
        return f"{self._name}: {self._cost}, {self._nest}, {self._possible_habitats}"

    def __repr__(self) -> str:
        return self.__str__()

    # def __eq__(self, __o: object) -> bool:
    #     o._name == self._name