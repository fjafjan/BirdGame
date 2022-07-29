import enum
from Player import Player
from Board import Board
from Types import Action, BirdFeederDice, FoodTypes, Habitat
from Card import Card

from typing import Dict, List

## Utility function used a lot. Not convinced this is better than nothing having it?
def choose_option(options: List, prompt: str, descr: str) -> int:
    """
    Prompts the user to choose one of the options in the list. 
    Returns the index of the chosen option or raises an exception if
    an invalid choice was made.
    """
    print(prompt)
    for index, op in options:
        print(f"{descr} #{index} : {op}")
    chosen_op = int(input())
    if 0 > chosen_op >= len(options):
        raise Exception(f"Invalid choice {chosen_op}.")
    # TODO change this to a debug print!
    print(f"Chosen {descr}: {chosen_op}")
    return chosen_op

class CommandlinePlayer(Player):
    def __init__(self) -> None:
        self._input_function = input
        self._board = None
        super().__init__()
    
    def initialize(self, board: Board) -> None:
        self._board = board
    
    def board(self) -> Board:
        return self._board

    def choose_action_to_take(self, possible_actions: List[Action]) -> Action:
        """
        Prompts the user to select an action.
        """
        print("Select an action: ")
        for index, action in enumerate(possible_actions):
            print(f"Action #{index}: {action}")
        chosen_action = possible_actions[int(self._input_function())]
        print(f"Chosen action: {chosen_action}")
        return chosen_action

    def choose_card_to_draw(self, birds_in_shop: List[Card]) -> Card:
        print("Select a card:")
        for index, bird_card in enumerate(birds_in_shop):
            print(f"Bird: #{index} : {bird_card}")
        print(f"#{index+1} : Deck (unknown bird)")
        chosen_bird = int(self._input_function())
        if chosen_bird == index+1:
            return None
        else:
            return birds_in_shop[chosen_bird]

    def choose_bird_to_lay_egg(self, birds_with_free_capacity: List[Card]) -> Card:
        print("Select bird to lay egg on:")
        for index, bird_card in enumerate(birds_with_free_capacity):
            print(f"#{index} : {bird_card._name}")
        chosen_bird = int(self._input_function())

        if 0 <= chosen_bird  < len(birds_with_free_capacity):
            return birds_with_free_capacity[chosen_bird]
        else:
            raise Exception(f"Invalid choice {chosen_bird}, choose between 0-{len(birds_with_free_capacity)-1}")

    ## TODO add type hints for this return type.
    def choose_bird_to_play(self, playable_birds: Dict[Card, Habitat]):
        print("Select which bird to play: Playable birds are")
        for i, bird in enumerate(playable_birds):
            print(f"#{i} : {bird}")
        chosen_bird = int(self._input_function())
        for i, bird in enumerate(playable_birds):
            if i == chosen_bird:
                chosen_bird = bird
        possible_habitats = playable_birds[chosen_bird]
        if len(possible_habitats) > 1:
            print(f"Select which habitat to play {chosen_bird._name}:")
            for i, habitat in enumerate(possible_habitats):
                print(f"#{i}: {habitat}")
            chosen_habitat = possible_habitats[int(self._input_function())]
        else:
            chosen_habitat = possible_habitats[0]
        print(f"Playing {chosen_bird} in {chosen_habitat}")
        return (chosen_bird, chosen_habitat)

    def choose_food_dice(self, bird_feeder_dice: List[BirdFeederDice], num_dice: int) -> List[BirdFeederDice]:
        print("Select food dice from the birdfeeder")
        ret = []
        for i in range(0, num_dice):
            for index, die in enumerate(bird_feeder_dice):
                print(f"#{index}: {die}")
            chosen_die = int(input())
            ret.append(bird_feeder_dice.pop(chosen_die))
        return ret

    def choose_grain_or_invertebret(self) -> FoodTypes:
        print("#0: Grain\n#1: Invertebret")
        chosen_food = int(self._input_function())
        return FoodTypes.GRAIN if chosen_food == 0 else FoodTypes.INVETEBRATE 

    def choose_starting_birds(self, starting_hand: List[Card]) -> List[Card]:
        print("Select what bird to keep")
        for index, bird_card in enumerate(starting_hand):
            print(f"Bird {index}: {bird_card}")

        ## function so we don't do the same parsing multiple times. 
        ## Todo move this to separate function, but of course should be replaced entirely.
        chosen_birds = self._input_function()
        kept_birds = []
        if chosen_birds.isdigit():
            kept_birds.append(int(chosen_birds))
        elif len(chosen_birds.split(",")) >= 2:
            kept_birds = {int(i) for i in chosen_birds.split(",")}
        elif len(chosen_birds.strip()) == 0:
            print("Are you sure you want to keep zero birds? Y/N")
            response = self._input_function()
            if response.upper() != "Y":
                print("Make up your mind!")
                exit(0)
        else:
            print("invalid argument")
            exit(1)
        your_hand = [starting_hand[i] for i in  kept_birds]
        return your_hand

    def choose_starting_food(self, starting_food: List[FoodTypes], num_food_to_keep: int):
        print(f"Select {num_food_to_keep} food to keep")
        for index, food_token in enumerate(starting_food):
            print(f"Food {index}: {food_token}")
        chosen_food = self._input_function()
        chosen_food = chosen_food.strip().split(",")
        chosen_food = [int(i) for i in chosen_food]
        if len(chosen_food) != num_food_to_keep:
            print(f"Choose {len(chosen_food)} insteadof {num_food_to_keep}")
        your_food = [starting_food[i] for i in chosen_food]
        return your_food
