from typing import List

from Card import Card
from Types import FoodTypes, Action, NestTypes, Habitat

def init_deck() -> List[Card]:
    deck = [
        Card("Pidgeon", [FoodTypes.GRAIN, FoodTypes.GRAIN], NestTypes.GROUND, [Habitat.ANY], 6),
        Card("Raven", [FoodTypes.ANY, FoodTypes.FRUIT], NestTypes.BIG_STICKS, [Habitat.ANY], 3),
        Card("Seagull", [FoodTypes.FISH, FoodTypes.FISH], NestTypes.BIG_STICKS, [Habitat.OCEAN], 4),
        Card("Hummingbird", [FoodTypes.FRUIT], NestTypes.CAVITY, [Habitat.FOREST], 3),
        Card("Parkers Owl", [FoodTypes.RODENT, FoodTypes.INVETEBRATE], NestTypes.CAVITY, [Habitat.FOREST], 6)
    ]
    return deck

def init_food() -> List[FoodTypes]:
    food = [
        FoodTypes.GRAIN,
        FoodTypes.INVETEBRATE,
        FoodTypes.RODENT,
        FoodTypes.FISH,
        FoodTypes.FRUIT
    ]
    return food

def init_actions() -> List[Action]:
    actions = [
        Action.PLAY_BIRD,
        Action.GATHER_FOOD,
        Action.LAY_EGGS,
        Action.DRAW_CARDS
    ]
    return actions
