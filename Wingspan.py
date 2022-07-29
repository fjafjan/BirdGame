from typing import List
from CommandlinePlayer import CommandlinePlayer

from GameSetup import init_deck, init_food, init_actions
from Board import Board
from Player import Player
from Birdfeeder import BirdFeeder
# from CommandlinePlayer import CommandlinePlayer
from Types import Action, Habitat

## Utility function
# def request_set(input_list: List, message_str: str):
#     """Asks the user for a number of element from a list."""
#     for index, item in enumerate(input_list):
#         print(f"{index}: {item}")
#     chosen_elements = self.input_function()
#     selected_elements = set()
#     if chosen_elements.isdigit():
#         selected_elements.add(int(chosen_elements))
#     elif len(chosen_elements.strip().split(",")) >= 2:
#         selected_elements = {int(i) for i in chosen_elements.split(",")}
#     return selected_elements

class Wingspan:
    def __init__(self, players: List[Player]):
        self._deck = init_deck()
        self._players = players
        self._bird_feeder = BirdFeeder()

    def setup(self):
        for player in self._players:
            starting_food = init_food()
            starting_hand = self._deck.draw_cards(5)
            print("Starting hand is:", starting_hand)
            chosen_birds = player.choose_starting_birds(starting_hand)
            print("Kept birds are:", chosen_birds)
            num_food_to_keep = 5-len(chosen_birds)
            chosen_food = player.choose_starting_food(starting_food, num_food_to_keep)
            print("Kept food is: ", chosen_food)

            # Of course we want to replace this eventually.
            board = Board(chosen_birds, chosen_food)
            player.initialize(board)
        self._deck.initialize()
        self._bird_feeder.reroll()

    def activate_birds(self, player: Player, board: Board, habitat: Habitat) -> None:
        """
        Activates all the birds in the chosen habitat.
        """
        birds_in_habitat = board.birds_in_habitat(habitat)
        # Go in reverse order
        birds_in_habitat.reverse()
        for bird in birds_in_habitat:
            print(f"Trying to activate {bird.name()}")
            bird.activate(board, player)

    def play_bird(self, player: Player, board: Board) -> None:
        """
        Plays a bird in the chosen habitat
        """
        playable_birds = board.playable_birds()
        if len(playable_birds) == 0:
            print("No playable birds")
        bird, habitat = player.choose_bird_to_play(playable_birds)
        print(f"bird: {bird}, habitat: {habitat}")
        board.play_bird(bird, habitat, player)

    def gather_food(self, player: Player, board: Board) -> None:
        """
        Gathers food and activates birds in the habitat.
        """
        food_dice = player.choose_food_dice(self._bird_feeder.dice(), 1)
        gained_food = self._bird_feeder.choose_dice(food_dice[0], player)
        board.gain_food(gained_food)
        # gained_food = [self._bird_feeder.choose_dice(die, player) for die in food_dice]
        # [board.gain_food(food) for food in gained_food]
        self.activate_birds(player, board, Habitat.FOREST)

    def lay_eggs(self, player: Player, board: Board) -> None:
        num_eggs = 2
        for _ in range(num_eggs):
            ## Would be nice if we had the option to lay multiple eggs here realistically.
            eggable_birds = board.eggable_birds()
            chosen_bird = player.choose_bird_to_lay_egg(eggable_birds)
            chosen_bird.lay_egg()
        self.activate_birds(player, board, Habitat.FIELD)

    def draw_cards(self, player: Player, board: Board) -> None:
        num_cards = 1
        ## TODO handle drawing more than one card here!
        chosen_card = player.choose_card_to_draw(self._deck.face_up_cards())
        # This corresponds to drawing from the deck.
        if chosen_card == None:
            board.draw_card(self._deck.draw_cards(1))
        else:
            board.draw_card(self._deck.draw_face_up(chosen_card))
        self.activate_birds(player, board, Habitat.OCEAN)
        ## Refill face up cards at end of turn.
        self._deck.refill_face_up()

    def play(self):
        possible_actions = init_actions()
        ## Now we are actually in the game phase!
        ## We do not yet have the concept of a round, or turn. Lets just have an infinite
        ## loop for now.
        while True:
            for player in self._players:
                board = player.board()
                action = player.choose_action_to_take(possible_actions)
                if action == Action.PLAY_BIRD:
                    self.play_bird(player, board)
                elif action == Action.GATHER_FOOD:
                    self.gather_food(player, board)
                elif action == Action.LAY_EGGS:
                    self.lay_eggs(player, board)
                elif action == Action.DRAW_CARDS:
                    self.draw_cards(player, board)






if __name__ == "__main__":
    players = [CommandlinePlayer()]
    game = Wingspan(players)
    game.setup()
    game.play()
    # initial_board = Board()