from typing import List

from GameSetup import init_deck, init_food, init_actions
from Board import Board

## Utility function
def request_set(input_list: List, message_str: str):
    """Asks the user for a number of element from a list."""
    for index, item in enumerate(input_list):
        print(f"{index}: {item}")
    chosen_elements = input()
    selected_elements = set()
    if chosen_elements.isdigit():
        selected_elements.add(int(chosen_elements))
    elif len(chosen_elements.strip().split(",")) >= 2:
        selected_elements = {int(i) for i in chosen_elements.split(",")}
    return selected_elements



class Wingspan:
    def __init__(self):
        deck = init_deck()
        your_food = init_food()
        your_hand = deck[0:5]
        print("Select what bird to keep")
        for index, bird_card in enumerate(your_hand):
            print(f"Bird {index}: {bird_card}")

        ## So what we need in order to make this testable?
        ## I guess we want to move all the logic away from this function, make a parsing 
        ## function so we don't do the same parsing multiple times. 
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
        num_food_to_keep = 5-len(kept_birds)
        print("Kept birds are:", your_hand)
        print(f"Select {num_food_to_keep} food to keep")
        for index, food_token in enumerate(your_food):
            print(f"Food {index}: {food_token}")
        chosen_food = input()
        chosen_food = chosen_food.strip().split(",")
        chosen_food = [int(i) for i in chosen_food]
        if len(chosen_food) != num_food_to_keep:
            print(f"Chose {len(chosen_food)} insteadof {num_food_to_keep}")
        your_food = [your_food[i] for i in chosen_food]
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
    # def choose_birds():






if __name__ == "__main__":
    Wingspan()
    # initial_board = Board()