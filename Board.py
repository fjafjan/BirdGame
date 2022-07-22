from typing import List

from Types import FoodTypes, Habitat, MAX_BIRDS_PER_HABITAT
from Card import Card
from FoodCost import FoodCost

class BonusCard:
    def __init__(self) -> None:
        """TODO"""
        pass

def egg_cost_from_slot(slot: int) -> int:
    if slot == 0:
        return 0
    elif 1 <= slot <= 2:
        return 1
    elif 3 <= slot <= 4:
        return 2
    else:
        raise Exception(f"Invalid slot {slot}")

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
        self._food_tokens = starting_food
        self._hand = starting_hand
        self._bonus_cards = []
        if (len(self._food_tokens) + len(self._hand)) is not 5:
            raise Exception(f"""Played should start with 5 total birds cards and food tokens, 
            not {len(self._food_tokens)} bird cards and {len(self._hand)} food token""")

    def draw_card(self, bird_card: Card):
        self._hand.append(bird_card)

    def draw_bonus_card(self, bonus_card: BonusCard):
        self._bonus_cards.append(bonus_card)



    def playable(self, bird_card: Card):
        """
        If a bird card is playable in the given board state.
        TODO maybe should change this so it returns the possible habitats!
        """
        ## Do we have enough food?
        if not bird_card.cost.within_budget(self._food_tokens):
            print("Too expensive, we cannot afford it")
            return False
        ## Is there space in any habitat?
        # habitats = [Habitat.FIELD, Habitat.FOREST, Habitat.OCEAN] if bird_card.possible_habitats == Habitat.ANY
        ## TODO replace with a list of habitats in the card constructor
        egg_costs = [0] * len(bird_card.possible_habitats)
        for index, habitat in enumerate(bird_card.possible_habitats):
            if len(self.habitat_slots[habitat]) < MAX_BIRDS_PER_HABITAT:
                print(f"Playable in {habitat}")
                egg_costs[index] = egg_cost_from_slot(len(self.habitat_slots[habitat]))
        ## TODO check for eggs!
        return True

    def total_eggs(self) -> int:
        """Counts the total number of eggs on birds"""
        total_eggs = 0
        for habitat in self.habitat_slots:
            for bird in self.habitat_slots[habitat]:
                total_eggs += bird.eggs()

    def bird_cards(self) -> List[Card]:
        """
        Returns a list of bird cards currently in your hand.
        """
        return self._hand

    def bonus_cards() -> List[BonusCard]:
        """
        Returns a list of bonus cards currently in your hand
        """
# Do we want this to be a class?
## So the way to do this, has to be to get a working super simple demo as quickly as
## possible.

## TODO Make this part of some other component!
