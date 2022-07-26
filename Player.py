from Card import Card

from typing import List

from Types import Action

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

    def choose_eggs_to_spend(birds_with_eggs: List[Card], number_of_eggs: int):
        """
        Choose eggs to remove from a bird.
        """
        pass

    def choose_bird_to_lay_egg(birds_with_free_capacity: List[Card], number_of_eggs: int):
        """
        Choose from any birds with egg capacity. Might be filtered in some other way.
        """
        pass

    def choose_card_to_draw(birds_in_shop: List[Card]):
        """
        Choose from the cards in the 'shop'
        """
        pass

    def choose_action_to_take(possible_actions: List[Action]):
        """
        Choose which action to take. 
        """
        pass