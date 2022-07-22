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

    def total_eggs(self) -> int:
        """Counts the total number of eggs on birds"""
        total_eggs = 0
        for habitat in self.habitat_slots:
            for bird in self.habitat_slots[habitat]:
                total_eggs += bird.eggs()
        return total_eggs

    def bird_cards(self) -> List[Card]:
        """
        Returns a list of bird cards currently in your hand.
        """
        return self._hand

    def bonus_cards() -> List[BonusCard]:
        """
        Returns a list of bonus cards currently in your hand
        """

    def playable_birds(self) -> List[Card]:
        """
        Returns all playable birds in yor hand
        """
        playable_birds = []
        eggs = self.total_eggs()
        ## Do we have enough food?
        for bird_card in self._hand:
            if not bird_card.cost.within_budget(self._food_tokens):
                print("Too expensive, we cannot afford it")
                continue
            ## Is there space in any habitat? And if so do we have enough eggs.
            egg_costs = [0] * len(bird_card.possible_habitats)
            for index, habitat in enumerate(bird_card.possible_habitats):
                if len(self.habitat_slots[habitat]) < MAX_BIRDS_PER_HABITAT:
                    egg_costs[index] = egg_cost_from_slot(len(self.habitat_slots[habitat]))
                    if egg_costs[index] <= eggs:
                        print(f"Playable in {habitat}")
                        playable_birds.append(bird_card)                    
            ## TODO Return the habitats we can play it in.
        return playable_birds

    def eggable_birds(self) -> List[Card]:
        """
        Returns all birds with at least one free egg slot
        """
        eggable_birds = []
        for habitat in self.habitat_slots:
            for bird in self.habitat_slots[habitat]:
                if bird.has_egg_slot():
                    eggable_birds.append(bird)
        return eggable_birds

