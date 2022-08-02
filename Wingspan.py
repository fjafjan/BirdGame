from typing import List
from CommandlinePlayer import CommandlinePlayer
from Deck import Deck

from GameSetup import init_deck, init_food, init_actions
from Board import Board
from Player import Player
from Birdfeeder import BirdFeeder
from Types import Action, Habitat

class Wingspan:
    def __init__(self, players: List[Player]):
        self._deck = init_deck()
        self._players = players
        self._bird_feeder = BirdFeeder()

    # Some getters.
    def deck(self) -> Deck:
        """
        Returns the deck instance which manages the face up and face down bird cards as
        well as the discard pile.
        """
        return self._deck

    def bird_feeder(self) -> BirdFeeder:
        """
        Returns the bird feeder which manages the food dice
        """
        return self._bird_feeder

    def players(self) -> List[Player]:
        """
        Returns a list of all players.
        """
        return self._players

    def setup(self):
        """
        Player choose their starting cards and food, and game components
        are initialized.
        """
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
            # TODO fix this!
            bird.activate(board=board, player=player, wingspan=self)

    def play_bird(self, player: Player, board: Board) -> None:
        """
        Plays a bird in the chosen habitat
        """
        playable_birds = board.playable_birds()
        bird, habitat = player.choose_bird_to_play(playable_birds)
        print(f"bird: {bird}, habitat: {habitat}")
        bird.play() # Activate any 'on play' power.
        board.play_bird(bird, habitat, player)

    def gather_food(self, player: Player, board: Board) -> None:
        """
        Gathers food and activates birds in the forest habitat.
        """
        active_slot = len(board.birds_in_habitat(Habitat.FOREST))
        optional_sacrifice = active_slot % 2 != 0

        extra_die = player.choose_sarifice_card_for_food() if optional_sacrifice else 0

        num_dice = 1 + extra_die + (active_slot // 2)
        food_dice = player.choose_food_dice(self._bird_feeder.dice(), num_dice)
        ## TODO re-write this with the nice for loop!
        for die in food_dice:
            gained_food = self._bird_feeder.choose_dice(die, player)
            board.gain_food(gained_food)
        self.activate_birds(player, board, Habitat.FOREST)

    def lay_eggs(self, player: Player, board: Board) -> None:
        """
        Lays eggs and activates birds in the field habitat.
        """
        active_slot = len(board.birds_in_habitat(Habitat.FIELD))
        optional_sacrifice = active_slot % 2 != 0
        extra_egg = player.choose_sacrifice_food_for_egg() if optional_sacrifice else 0
        num_eggs = 2 + extra_egg + (active_slot // 2)
        for _ in range(num_eggs):
            ## Would be nice if we had the option to lay multiple eggs here realistically.
            eggable_birds = board.eggable_birds()
            if len(eggable_birds) == 0:
                print("No birds to lay eggs on!")
                break
            chosen_bird = player.choose_bird_to_lay_egg(eggable_birds)
            chosen_bird.lay_egg()
        self.activate_birds(player, board, Habitat.FIELD)

    def draw_cards(self, player: Player, board: Board) -> None:
        """
        Draws cards from the face up birds or from the deck, and activates birds
        in the ocean habitat.
        """
        active_slot = len(board.birds_in_habitat(Habitat.FIELD))
        optional_sacrifice = active_slot % 2 != 0
        extra_card = player.choose_sacrifice_egg_for_card() if optional_sacrifice else 0
        num_cards = 1 + extra_card + (active_slot // 2)
        for _ in range(num_cards):
            chosen_card = player.choose_card_to_draw(self._deck.face_up_cards())
            # This corresponds to drawing from the deck.
            if chosen_card is None:
                board.draw_card(self._deck.draw_cards(1))
            else:
                board.draw_card(self._deck.draw_face_up(chosen_card))
        self.activate_birds(player, board, Habitat.OCEAN)
        ## Refill face up cards at end of turn.
        ## TODO Move this to an end of turn phase! We can also trigger other things like discarding cards there.
        self._deck.refill_face_up()

    def play(self):
        """
        Play the game until completion. Currently rounds are not implemented so gameplay
        continued indefinitely.
        """
        possible_actions = init_actions()
        ## Now we are actually in the game phase!
        ## We do not yet have the concept of a round, or turn. Lets just have an infinite
        ## loop for now.
        while True:
            for player in self._players:
                board = player.board()
                action = player.choose_action_to_take(possible_actions)
                if action == Action.PLAY_BIRD:
                    if len(board.playable_birds()) == 0:
                        print("No playable birds")
                        continue
                    self.play_bird(player, board)
                elif action == Action.GATHER_FOOD:
                    self.gather_food(player, board)
                elif action == Action.LAY_EGGS:
                    self.lay_eggs(player, board)
                elif action == Action.DRAW_CARDS:
                    self.draw_cards(player, board)






if __name__ == "__main__":
    players = [CommandlinePlayer("Player 0"), CommandlinePlayer("Player 1")]
    game = Wingspan(players)
    game.setup()
    game.play()
