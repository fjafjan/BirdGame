from typing import List

from Card import Card
from Types import Food, Action, Nest, Habitat
from Deck import Deck

## I guess we should define the powers outside as functions, and then pair them with the birds.
## Since a number of birds share the same power.

def init_deck() -> Deck:
    cards = [
        Card("Pigeon", [Food.GRAIN, Food.GRAIN], Nest.GROUND, [Habitat.ANY], 6), # Lay an egg on any bird.
        Card("Seagull", [Food.FISH, Food.FISH], Nest.PLATFORM, [Habitat.OCEAN], 4), # Draw an extra card?
        Card("Hummingbird", [Food.FRUIT], Nest.CAVITY, [Habitat.FOREST], 2), # Each player gains 1 dice from the birdfeeder.
        Card("Parkers Owl", [Food.RODENT, Food.INVETEBRATE], Nest.CAVITY, [Habitat.FOREST], 6), # Decide what it does :D
        Card("Painted Whitestart", [Food.INVETEBRATE], Nest.GROUND, [Habitat.FOREST], 3), # Gain 1 invertebret from the supply
        Card("Baltimore Oriole", [Food.FRUIT, Food.FRUIT, Food.INVETEBRATE], Nest.ANY, [Habitat.FOREST], 2), # All players gain 1 fruit from the supply
        Card("Grasshopper Sparrow", [Food.INVETEBRATE, Food.GRAIN], Nest.GROUND, [Habitat.FIELD], 2), # SHOULD BE EITHER OR FOOD. Lay 1 egg on any bird.
        Card("Black-billed Magpie", [Food.ANY, Food.ANY], Nest.ANY, [Habitat.FIELD], 3), # REACTION: When another players DEATH succeeds, gain 1 dice from teh birdfeeder.
        Card("Dickcissel", [Food.INVETEBRATE, Food.GRAIN, Food.GRAIN], Nest.GROUND, [Habitat.FIELD], 3), # Tuck a card, if you do lay 1 egg on this bird.
        Card("Violet-green Swallow", [Food.INVETEBRATE, Food.INVETEBRATE], Nest.CAVITY, [Habitat.ANY], 3), # Tuck a card behind this card, if you do draw 1 card.
        Card("Purple Martin", [Food.INVETEBRATE], Nest.CAVITY, [Habitat.FIELD, Habitat.OCEAN], 3), # Tuck a card behind this card, if you do draw a card.
        Card("American Coot", [Food.ANY, Food.GRAIN], Nest.PLATFORM, [Habitat.OCEAN], 5) # Tuck a card behind this card, if you do draw a card.
    ]
    return Deck(cards)

def init_food() -> List[Food]:
    food = [
        Food.GRAIN,
        Food.INVETEBRATE,
        Food.RODENT,
        Food.FISH,
        Food.FRUIT
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
