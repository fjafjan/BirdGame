"""
Gulls are some of the most powerful cards and might need to be nerfed
in one way or another. Similar to corvids they allow you to sacrifice one
resource for another, but where the corvids sacrifice eggs for food, the
gulls sacrifice eggs for cards.
"""

from Card import Card
from Player import Player
from Board import Board
from Wingspan import Wingspan

def gull_power(this_bird: Card, player: Player, board: Board, wingspan: Wingspan):
    """
    Remove an egg from any bird (?) to draw 1 or 2 cards.
    """
    birds_with_eggs = board.birds_with_eggs()
    birds_with_spent_eggs = player.choose_eggs_to_spend(birds_with_eggs, 1)
    for bird in birds_with_spent_eggs:
        bird.remove_egg()
    birds_in_shop = wingspan.deck().face_up_cards()
    for _ in range(2):
        chosen_card = player.choose_card_to_draw(birds_in_shop)
        # This corresponds to drawing from the deck.
        if chosen_card is None:
            board.draw_card(wingspan.deck().draw_cards(1))
        else:
            board.draw_card(wingspan.deck().draw_face_up(chosen_card))
