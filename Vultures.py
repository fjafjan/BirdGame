"""
Carrion eating birds require no food, but have no activation function.
An interesting option to quickly fill your birds and access the more powerful
powers in the third slot.
"""

from Card import Card
from Player import Player
from Board import Board
from Wingspan import Wingspan

def carrion_on_play(_: Card, player: Player, board: Board, wingspan: Wingspan):
    """
    When played draw two bonus cards and select one.
    """
    ## So we need to access the entire game state to draw cards! Or to gain food
    ## from the birdfeeder.

    # bonus_cards = swingspan.draw_bonus_cards(2)
    # chosen_bonus_card = player.choose_bonus_card(bonus_cards)
    board.draw_bonus_card(None)
