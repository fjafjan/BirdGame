from Card import Card
from Types import Action, Food, Habitat, BirdFeederDice

from typing import Dict, List


## This is the operative class, i.e. the person making decisions.
## So any request for choice should be delegated to a player class.

## Realistically we will want at least 3 types of players.

## 1) The text based player, i.e. the first prototype version.
## 2) The AI player. Initially this can be as stupid as possible and just perform
##    random valid actions. Of course potentially infinite potention to make a clever AI.
## 3) The UI player. If/when there is a UI, we want these decisions to be made via the UI.
## 4) The remote player. This can be either text based on UI, but performed remotely, i.e. we
##    don't know. But if the player implementation is agnostic then it should be fine!

class Player:
    def __init__(self) -> None:
        pass

    def initialize(self, board: object):
        """
        Intialize your game board with the chosen birds and food.
        """
        pass

    def board(self):
        """
        Return board of the player.
        """
        pass

    def choose_starting_birds(self, starting_hand: List[Card]) -> List[Card]:
        """
        Select which starting birds to keep from an initial hand.
        """
        pass

    def choose_starting_food(self, starting_food: List[Food], num_food_to_keep: int) -> List[Food]:
        """
        Select which of the starting food to keep, given a number of birds cards you have selected
        """
        pass

    def choose_action_to_take(self, possible_actions: List[Action]) -> Action:
        """
        Choose which action to take.
        """
        pass

    def choose_bird_to_lay_egg(self, birds_with_free_capacity: List[Card]) -> Card:
        """
        Choose from any birds with egg capacity. Might be filtered in some other way.
        """
        pass

    def choose_bird_to_play(self, playable_birds: Dict[Card, Habitat]):
        """
        Choose what playable bird to play.
        """
        pass

    def choose_card_to_draw(self, birds_in_shop: List[Card]) -> Card:
        """
        Choose from the cards in the 'shop'
        """
        pass

    def choose_eggs_to_spend(self, birds_with_eggs: List[Card], number_of_eggs: int) -> Dict[Card, int]:
        """
        Choose eggs to remove from a bird.
        """
        pass

    def choose_food_dice(self, bird_feeder_dice: List[BirdFeederDice], num_dice: int) -> List[BirdFeederDice]:
        """
        Choose which bird feeder dice to be used for getting food
        """
        pass

    def choose_grain_or_invertebret(self) -> Food:
        """
        Choose wether to pick grain or invertebret
        """
        pass