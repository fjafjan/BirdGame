from typing import List

from Card import Card
from Types import FoodTypes, Action, NestTypes, Habitat

## I guess we should define the powers outside as functions, and then pair them with the birds. 
## Since a number of birds share the same power. 

def init_deck() -> List[Card]:
    deck = [
        Card("Pigeon", [FoodTypes.GRAIN, FoodTypes.GRAIN], NestTypes.GROUND, [Habitat.ANY], 6), # Lay an egg on any bird.
        Card("Raven", [FoodTypes.ANY, FoodTypes.FRUIT], NestTypes.PLATFORM, [Habitat.ANY], 3), # the worse raven power, i.e. sack one egg, gain 1 food.
        Card("Seagull", [FoodTypes.FISH, FoodTypes.FISH], NestTypes.PLATFORM, [Habitat.OCEAN], 4), # Draw an extra card?
        Card("Hummingbird", [FoodTypes.FRUIT], NestTypes.CAVITY, [Habitat.FOREST], 2), # Each player gains 1 dice from the birdfeeder.  
        Card("Parkers Owl", [FoodTypes.RODENT, FoodTypes.INVETEBRATE], NestTypes.CAVITY, [Habitat.FOREST], 6), # Decide what it does :D 
        Card("Painted Whitestart", [FoodTypes.INVETEBRATE], NestTypes.GROUND, [Habitat.FOREST], 3), # Gain 1 invertebret from the supply
        Card("Baltimore Oriole", [FoodTypes.FRUIT, FoodTypes.FRUIT, FoodTypes.INVETEBRATE], NestTypes.ANY, [Habitat.FOREST], 2), # All players gain 1 fruit from the supply
        Card("Grasshopper Sparrow", [FoodTypes.INVETEBRATE, FoodTypes.GRAIN], NestTypes.GROUND, [Habitat.FIELD], 2), # SHOULD BE EITHER OR FOOD. Lay 1 egg on any bird.
        Card("Black-billed Magpie", [FoodTypes.ANY, FoodTypes.ANY], NestTypes.ANY, [Habitat.FIELD], 3), # REACTION: When another players DEATH succeeds, gain 1 dice from teh birdfeeder.
        Card("Dickcissel", [FoodTypes.INVETEBRATE, FoodTypes.GRAIN, FoodTypes.GRAIN], NestTypes.GROUND, [Habitat.FIELD], 3), # Tuck a card, if you do lay 1 egg on this bird.
        Card("Violet-green Swallow", [FoodTypes.INVETEBRATE, FoodTypes.INVETEBRATE], NestTypes.CAVITY, [Habitat.ANY], 3), # Tuck a card behind this card, if you do draw 1 card.
        Card("Purple Martin", [FoodTypes.INVETEBRATE], NestTypes.CAVITY, [Habitat.FIELD, Habitat.OCEAN], 3), # Tuck a card behind this card, if you do draw a card.
        Card("American Coot", [FoodTypes.ANY, FoodTypes.GRAIN], NestTypes.PLATFORM, [Habitat.OCEAN], 5) # Tuck a card behind this card, if you do draw a card.
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
