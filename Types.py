from enum import Enum

class FoodTypes(Enum):
    ANY = 0
    INVETEBRATE = 1
    GRAIN = 2
    FISH = 3
    RODENT = 4
    FRUIT = 5

class NestTypes(Enum):
    ANY = 0 
    GROUND = 1
    CAVITY = 2
    BOWL = 3
    PLATFORM = 3

MAX_BIRDS_PER_HABITAT = 6

class Habitat(Enum):
    ANY = 0
    FOREST = 1
    FIELD = 2
    OCEAN = 3

class Action(Enum):
    PLAY_BIRD = 0,
    GATHER_FOOD = 1,
    LAY_EGGS = 2,
    DRAW_CARDS = 3
