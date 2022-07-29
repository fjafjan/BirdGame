from typing import List

from GameSetup import init_deck, init_food, init_actions
from Board import Board
from Card import Card
from Player import Player
# from CommandlinePlayer import CommandlinePlayer
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
    def __init__(self, players: List[Player]):
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
            playable_birds = your_board.playable_birds()
            if len(playable_birds) == 0:
                print("No plabale birds")
            else:
                print("Select which bird to play: Playable birds are")
                for i, bird in enumerate(playable_birds):
                    print(f"#{i} : {bird}")
                chosen_bird = int(self.input_function())
                for i, bird in enumerate(playable_birds):
                    if i == chosen_bird:
                        chosen_bird = bird
                possible_habitats = playable_birds[chosen_bird]
                if len(possible_habitats) > 1:
                    print(f"Select which habitat to play {chosen_bird._name}:")
                    for i, habitat in enumerate(possible_habitats):
                        print(f"#{i}: {habitat}")
                    chosen_habitat = possible_habitats[int(self.input_function())]
                else:
                    chosen_habitat = possible_habitats[0]
                print(f"Playing {chosen_bird} in {chosen_habitat}")
                ## TODO add a proper player here. 
                your_board.play_bird(chosen_bird, chosen_habitat, Player())
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