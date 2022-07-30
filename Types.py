"""
Basic components and resources used in the game.
"""
from enum import Enum

class Food(Enum):
    """
    Food spent to play bird cards, or sometimes cached on cards.
    """
    ANY = 0
    INVETEBRATE = 1
    GRAIN = 2
    FISH = 3
    RODENT = 4
    FRUIT = 5

class BirdFeederDice(Enum):
    """
    The faces of the bird feeder dice corresponding to different food can that be gained.
    """
    GRAIN = 0
    INVETEBRET = 1
    GRAIN_OR_INVETEBRET = 2
    FISH = 3
    RODENT = 4
    FRUIT = 5

class Nest(Enum):
    """
    The differnt types of bird nests. Primarily used for bonus cards or end of round scoring.
    """
    ANY = 0
    GROUND = 1
    CAVITY = 2
    BOWL = 3
    PLATFORM = 3

MAX_BIRDS_PER_HABITAT = 6

class Habitat(Enum):
    """
    The habitats where birds can be played, also corresponding to different actions.
    """
    ANY = 0
    FOREST = 1
    FIELD = 2
    OCEAN = 3

class Action(Enum):
    """
    The four actions that can be taken each turn.
    """
    PLAY_BIRD = 0,
    GATHER_FOOD = 1,
    LAY_EGGS = 2,
    DRAW_CARDS = 3
