from enum import Enum
from typing import List, Dict
print("Hello")

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
    BIG_STICKS = 3

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

class FoodCost:
    """
    Describes a comparable class of a food cost. 
    """
    def __init__(self, cost: List[FoodTypes]=[]):
        self.cost = {
            FoodTypes.ANY: 0,
            FoodTypes.INVETEBRATE: 0, 
            FoodTypes.GRAIN : 0,
            FoodTypes.FISH : 0,
            FoodTypes.RODENT : 0,
            FoodTypes.FRUIT : 0
        }
        for food_type in cost:
            self.cost[food_type] += 1
        print("Food input:", cost)
        print("My food map is:", self.cost)

    def less_than(self, food: List[FoodTypes]=[]) -> True:
        ## Not entirel sure my logic is correct here but lets write 
        ## a simple method and can write some tests later to make sure 
        ## it works as intended.
        available_food = FoodTypes(food)
        for food_type in self.cost:
            if self.cost[food_type] > available_food[food_type]:
                print(f"Not enough {food_type}")
                return False
        return True
    def __str__(self):
        return f"{self.cost}"
class Card:
    """
    Describes a bird card. Each bird card has a unique name, a cost in food, 
    a nest type and a list of possible habitats in can live in. 
    """
    def __init__(self, name: str, cost: List[FoodTypes], nest: NestTypes, possible_habitats: List[Habitat]):
        self.name = name
        self.cost = FoodCost(cost)
        self.nest = nest
        self.possible_habitats = possible_habitats
    def __str__(self):
        return f"{self.name}: {self.cost}, {self.nest}, {self.possible_habitats}"


class Board:
    """
    Defines the board state of a player, 
    consisting of their available resources, cards in hand, available 
    food tokens.
    """
    def __init__(self, starting_hand: List[Card], starting_food: List[FoodTypes]):
        self.habitat_slots = {
            Habitat.FIELD : [],
            Habitat.FOREST : [],
            Habitat.OCEAN : []
        }
        # self.forest = []
        # self.field = []
        # self.ocean = []
        ## What is the best data structure for this? Should probably 
        ## just be hardcoded
        ## Should rename it from food cost!
        self.food_tokens = FoodCost(starting_food)
        self.hand = starting_hand
    def playable(self, bird_card: Card) -> bool:
        
        ## Do we have enough food?
        if not self.food_tokens.less_than(food=bird_card.cost):
            print("Too expensive, we cannot afford it")
            return False
        ## Is there space in any habitat?
        # habitats = [Habitat.FIELD, Habitat.FOREST, Habitat.OCEAN] if bird_card.possible_habitats == Habitat.ANY
        ## TODO replace with a list of habitats in the card constructor
        for habitat in bird_card.possible_habitats:
            if len(self.habitat_slots[habitat]) < MAX_BIRDS_PER_HABITAT:
                print(f"Playable in {habitat}")

        ## TODO check for eggs!        
        return True
        print("Not playable")

# Do we want this to be a class?
## So the way to do this, has to be to get a working super simple demo as quickly as 
## possible. 

## TODO Make this part of some other component!

def init_deck() -> List[Card]:
    deck = [
        Card("Pidgeon", [FoodTypes.GRAIN, FoodTypes.GRAIN], NestTypes.GROUND, Habitat.ANY),
        Card("Raven", [FoodTypes.ANY, FoodTypes.FRUIT], NestTypes.BIG_STICKS, Habitat.ANY),
        Card("Seagull", [FoodTypes.FISH, FoodTypes.FISH], NestTypes.BIG_STICKS, Habitat.OCEAN),
        Card("Hummingbird", [FoodTypes.FRUIT], NestTypes.CAVITY, Habitat.FOREST),
        Card("Parkers Owl", [FoodTypes.RODENT, FoodTypes.INVETEBRATE], NestTypes.CAVITY, Habitat.FOREST)
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

class Wingspan:
    def __init__(self):
        deck = init_deck()
        your_food = init_food()
        your_hand = deck[0:5]
        print("Select what bird to keep")
        for index, bird_card in enumerate(your_hand):
            print(f"Bird {index}: {bird_card}")
        
        ## Todo move this to separate function, but of course should be replaced entirely. 
        chosen_birds = input()
        kept_birds = []
        if chosen_birds.isdigit():
            kept_birds.append(int(chosen_birds))
        elif len(chosen_birds.split(",")) >= 2:
            kept_birds = {int(i) for i in chosen_birds.split(",")}
        elif len(chosen_birds.strip()) == 0:
            print("Are you sure you want to keep zero birds? Y/N")
            response = input()
            if response.upper() != "Y":
                print("Make up your mind!")
                exit(0)
        else:
            print("invalid argument")
            exit(1)
        your_hand = [your_hand[i] for i in  kept_birds]
        num_food_to_keep = {5-len(kept_birds)}
        print("Kept birds are:", your_hand)
        print(f"Select {num_food_to_keep} food to keep")
        for index, food_token in enumerate(your_food):
            print(f"Food {index}: {food_token}")
        chosen_food = input()
        chosen_food.strip().split(",")
        if len(chosen_food) != num_food_to_keep:
            print("Chose {len(chosen_food)} insteadof {num_food_to_keep}")
        your_food = chosen_food
        print("Kept food is: ", your_food)

        # Of course we want to replace this eventually.
        possible_actions = init_actions()
        your_board = Board(your_hand, your_food)
        print("Select an action: ")
        for index, action in enumerate(possible_actions):
            print(f"Action {index}: {action}")
        chosen_action = input()
        if chosen_action == "0":
            playable_birds = [bird for bird in your_hand if your_board.playable(bird)]
            print("Playable birds are", playable_birds)
            # for index, bird in your_hand:
            #     if bird.is_playable():
            #         print("")
        ## Okay but now we need to break this out into smarter components 
        ## and check if we can do this! 
        ## So what does it mean to play a bird?
        ## Well for each possible bird in your hand, you can check if it is playable. 
    def choose_birds():
        


             



Wingspan()

initial_board = Board()