"""
Ravens are intelligent birds with a powerful ability, exchanging
eggs for food. To limit this power they can not use eggs laid on
themseles meaning you need to play at least one other bird to utilize
their power
"""

from Card import Card
from Player import Player
from Board import Board

from Types import Food, Nest, Habitat

## TODO we would like an alternative like std::bind in c++ here to fix num_food
##      for the different birds.
def corvid_power(this_bird: Card, player: Player, board: Board, num_food: int):
    """
    Discard one egg from another bird to gain N food..
    """
    birds_with_eggs = board.birds_with_eggs()
    # Remove the current bird
    if this_bird in birds_with_eggs:
        birds_with_eggs.remove(this_bird)
    birds_with_spent_eggs = player.choose_eggs_to_spend(birds_with_eggs, 1)
    for bird in birds_with_spent_eggs:
        bird.remove_egg()



ravens = [
    Card("Chichuacha Raven", [Food.ANY, Food.ANY, Food.FRUIT], Nest.PLATFORM, [Habitat.ANY], 3, corvid_power), # the worse raven power, i.e. sack one egg, gain 1 food.
    Card("Scottish Raven", [Food.ANY, Food.ANY, Food.FISH], Nest.PLATFORM, [Habitat.OCEAN], 2, corvid_power),
    Card("Common Raven", [Food.ANY, Food.INVETEBRATE], Nest.PLATFORM, [Habitat.ANY], 3, corvid_power)
]