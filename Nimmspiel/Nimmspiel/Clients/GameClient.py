class Spieler:
    def __init__(self, game):
        self.game = game

    def run(self):
        self.game.play()
