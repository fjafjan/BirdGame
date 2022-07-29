# from scipy import rand
from Card import Card

from typing import List
import random

class Deck:
    """
    Simple class for abstracting the deck.
    """
    def __init__(self, cards: List[Card]) -> None:
        self._cards = cards
        self._discard_pile = []
        self._face_up = []

    def initialize(self):
        self._face_up = [self._cards.pop(0) for i in range(3)]

    def reshuffle(self):
        """Shuffles the discard pile into the draw pile"""
        ### TODO Use a better seed?
        self._cards = self._discard_pile.copy()
        random.shuffle(self._cards())

    def draw_cards(self, num_cards: int) -> List[Card]:
        """Draws the requested number of cards from the deck"""
        if len(self._cards) < num_cards:
            cards_left = num_cards - len(self._cards)
            ret = [self._cards.pop(0) for i in range(len(self._cards))]
            self.reshuffle()
            ret.extend([self._cards.pop(0) for i in range(cards_left)])
        else:
            ret = [self._cards.pop(0) for i in range(num_cards)]
        return ret

    def discard_cards(self, cards: List[Card]) -> None:
        """Return cards that were for various reasons discarded into the discard pile"""
        self._discard_pile.extend(cards)

    def face_up_cards(self) -> List[Card]:
        """Three face up cards always visible."""
        return self._face_up

    def draw_face_up(self, card: Card) -> Card:
        """Draws a card from the face-up cards"""
        if card not in self._face_up:
            raise Exception(f"{card} not among the face up cards!")
        else:
            i = self._face_up.index(card)
            self._face_up[i] = None
        return card

    def refill_face_up(self) -> None:
        """
        Refills face up cards. Only done at end of turn.
        """
        for index, card in enumerate(self._face_up):
            if card == None:
                self._face_up[index] = self.draw_cards(1)[0]

    def reset_face_up(self) -> None:
        """
        Between rounds, the face up cards are replaced.
        """
        self.discard_cards(self._face_up)
        self._face_up.clear()
        self._face_up = self.draw_cards(3)
