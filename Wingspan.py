from typing import List

from GameSetup import init_deck, init_food, init_actions
from Board import Board
from Card import Card
from Types import FoodTypes, Action

## Utility function
def request_set(input_list: List, message_str: str):
    """Asks the user for a number of element from a list."""
    for index, item in enumerate(input_list):
        print(f"{index}: {item}")
    chosen_elements = self.input_function()
    selected_elements = set()
    if chosen_elements.isdigit():
        selected_elements.add(int(chosen_elements))
    elif len(chosen_elements.strip().split(",")) >= 2:
        selected_elements = {int(i) for i in chosen_elements.split(",")}
    return selected_elements



class Wingspan:
    def choose_starting_birds(self, starting_hand: List[Card]) -> List[Card]:
        print("Select what bird to keep")
        for index, bird_card in enumerate(starting_hand):
            print(f"Bird {index}: {bird_card}")

        ## function so we don't do the same parsing multiple times. 
        ## Todo move this to separate function, but of course should be replaced entirely.
        chosen_birds = self.input_function()
        kept_birds = []
        if chosen_birds.isdigit():
            kept_birds.append(int(chosen_birds))
        elif len(chosen_birds.split(",")) >= 2:
            kept_birds = {int(i) for i in chosen_birds.split(",")}
        elif len(chosen_birds.strip()) == 0:
            print("Are you sure you want to keep zero birds? Y/N")
            response = self.input_function()
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
        chosen_food = self.input_function()
        chosen_food = chosen_food.strip().split(",")
        chosen_food = [int(i) for i in chosen_food]
        if len(chosen_food) != num_food_to_keep:
            print(f"Chose {len(chosen_food)} insteadof {num_food_to_keep}")
        your_food = [starting_food[i] for i in chosen_food]
        return your_food

    def __init__(self, input_function = input):
        self.input_function = input_function
        deck = init_deck()
        starting_food = init_food()
        starting_hand = deck[0:5]
        your_hand = self.choose_starting_birds(starting_hand)
        print("Kept birds are:", your_hand)

        num_food_to_keep = 5-len(your_hand)
        your_food = self.choose_starting_food(starting_food, num_food_to_keep)
        print("Kept food is: ", your_food)

        # Of course we want to replace this eventually.
        possible_actions = init_actions()
        your_board = Board(your_hand, your_food)
        print("Select an action: ")
        for index, action in enumerate(possible_actions):
            print(f"Action {index}: {action}")
        chosen_action = int(self.input_function())


        if possible_actions[chosen_action] == Action.PLAY_BIRD:
            playable_birds = your_board.playable_birds
            if len(playable_birds) == 0:
                print("No plabale birds")
            else:
                print("Select which bird to play: Playable birds are")
                for i, bird in enumerate(playable_birds):
                    print("f#{i} : {bird}")
                chosen_bird = int(self.input_function())

            # for index, bird in your_hand:
            #     if bird.is_playable():
            #         print(""

        ## Okay but now we need to break this out into smarter components
        ## and check if we can do this!
        ## So what does it mean to play a bird?
        ## Well for each possible bird in your hand, you can check if it is playable.
    # def choose_birds():






if __name__ == "__main__":
    Wingspan()
    # initial_board = Board()