"""
Class for representing the birdfeeder. Could maybe be merged in to 
be a part of the "remaining game" components. 
"""

from enum import Enum
from typing import List

import random
import time

from Types import FoodTypes

class BirdFeederDice(Enum):
    GRAIN = 0
    INVETEBRET = 1,
    GRAIN_OR_INVETEBRET = 2
    FISH = 3
    RODENT = 4
    FRUIT = 5

class BirdFeeder:
    def __init__(self) -> None:
        self._dice = []
        self._rand = random.Random(time.time())

    def reroll(self):
        self._dice = [BirdFeederDice(self._rand.randint(0, 5)) for i in range(0,5)]
        print("Dice are:", self._dice)

    def dice(self) -> List[BirdFeederDice]:
        return self._dice
    
    ## I should decide what interface I want here. 
    def food_to_choose(self) -> List[FoodTypes]:
        """
        Returns a list of the possible foods that are avialable in the birdfeeder at the moment
        """
        ret = []]
        for dice in self._dice:
            if dice == BirdFeederDice.FISH:
                ret.append(FoodTypes.FISH)
            elif dice == BirdFeederDice.FRUIT
                ret.append(FoodTypes.FISH)
            elif dice == BirdFeederDice.GRAIN
                ret.append(FoodTypes.GRAIN)
            elif dice == BirdFeederDice.INVETEBRET
                ret.append(FoodTypes.INVETEBRATE)
            elif dice == BirdFeederDice.RODENT
                ret.append(FoodTypes.RODENT)
            elif dice == BirdFeederDice.GRAIN_OR_INVETEBRET:
                ret.append(FoodTypes.GRAIN)
                ret.append(FoodTypes.INVETEBRATE)
        ## Maybe I should just return a list of dice here and then prompt the user again?
        ## imo that makes a lot more sense. I will re-write this function when I actually use it.

    def choose_dice(self, chosen_die: BirdFeederDice):
        """
        Choose a dice from the birdfeeder. Will raise an exception if no such dice excists.
        """
        for i, die in enumerate(self._dice):
            if die == chosen_die:
                self._dice.remove(die)
                break
        else:
            raise Exception(f"No {chosen_die} in the birdfeeder!")

    def roll_dice_not_in_birdfeeder(self) -> List[BirdFeederDice]:
        """
        Rolls any dice not in the birdfeeder and returns the outcome.
        """
        num_dice_outside = 5 - len(self._dice)
        ret = [BirdFeederDice(self._rand.randint(0, 6)) for i in range(0, num_dice_outside)]
        return ret