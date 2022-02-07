from RPSLS.player import Player
from ai import AI
from human import Human

class Game(Player):
    def __init__(self):
        self.human = Human()
        self.ai = AI()
        super().__init__()

    def run_game(self):
        pass
    
    def display_rules(self):
        pass

    def begin_round(self):
        pass

    def display_move(self):
        pass

    def ai_turn(self):
        pass

    def human_turn(self):
        pass

    def record_results(self):
        pass

    def display_winner(self):
        pass





