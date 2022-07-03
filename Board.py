from typing import List

from Types import FoodTypes, Habitat, MAX_BIRDS_PER_HABITAT
from Card import Card
from FoodCost import FoodCost

class Board:
    """
    Defines the board state of a player,
    consisting of their available resources, cards in hand, available
    food tokens.
    """
    def __init__(self, starting_hand: List[Card], starting_food: List[FoodTypes]):
        self.habitat_slots = {
            Habitat.FIELD : [],
            Habitat.FOREST : [],
            Habitat.OCEAN : []
        }
        ## Should rename it from food cost!
        self.food_tokens = FoodCost(starting_food)
        self.hand = starting_hand
    def playable(self, bird_card: Card):
        """
        If a bird card is playable in the given board state.
        """
        ## Do we have enough food?
        if not self.food_tokens.within_budget(food=bird_card.cost):
            print("Too expensive, we cannot afford it")
            return False
        ## Is there space in any habitat?
        # habitats = [Habitat.FIELD, Habitat.FOREST, Habitat.OCEAN] if bird_card.possible_habitats == Habitat.ANY
        ## TODO replace with a list of habitats in the card constructor
        for habitat in bird_card.possible_habitats:
            if len(self.habitat_slots[habitat]) < MAX_BIRDS_PER_HABITAT:
                print(f"Playable in {habitat}")

        ## TODO check for eggs!
        return True
        print("Not playable")

# Do we want this to be a class?
## So the way to do this, has to be to get a working super simple demo as quickly as
## possible.

## TODO Make this part of some other component!
