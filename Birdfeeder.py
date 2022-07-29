"""
Class for representing the birdfeeder. Could maybe be merged in to
be a part of the "remaining game" components.
"""

from typing import List

import random
import time

from Types import FoodTypes, BirdFeederDice
from Player import Player

class BirdFeeder:
    def __init__(self) -> None:
        self._dice = []
        self._rand = random.Random(time.time())

    def reroll(self):
        self._dice = [BirdFeederDice(self._rand.randint(0, 5)) for i in range(0,5)]
        print("Dice are:", self._dice)

    def dice(self) -> List[BirdFeederDice]:
        return self._dice.copy()

    @staticmethod
    def birdfeeder_dice_to_foodtype(die: BirdFeederDice) -> FoodTypes:
        if die == BirdFeederDice.FISH:
            return FoodTypes.FISH
        elif die == BirdFeederDice.FRUIT:
            return FoodTypes.FRUIT
        elif die == BirdFeederDice.GRAIN:
            return FoodTypes.GRAIN
        elif die == BirdFeederDice.INVETEBRET:
            return FoodTypes.INVETEBRATE
        elif die == BirdFeederDice.RODENT:
            return FoodTypes.RODENT
        else:
            raise Exception(f"Cannot determine foodtype from {die}")

    def choose_dice(self, chosen_die: BirdFeederDice, player: Player) -> FoodTypes:
        """
        Choose a dice from the birdfeeder. Will raise an exception if no such dice excists.
        """
        for die in self._dice:
            if die == chosen_die:
                self._dice.remove(die)
                print(f"Removed {die}")
                if die == BirdFeederDice.GRAIN_OR_INVETEBRET:
                    return player.choose_grain_or_invertebret()
                else:
                    return self.birdfeeder_dice_to_foodtype(die)
        raise Exception(f"No {chosen_die} in the birdfeeder!")

    def roll_dice_not_in_birdfeeder(self) -> List[BirdFeederDice]:
        """
        Rolls any dice not in the birdfeeder and returns the outcome.
        """
        num_dice_outside = 5 - len(self._dice)
        ret = [BirdFeederDice(self._rand.randint(0, 5)) for i in range(0, num_dice_outside)]
        return ret