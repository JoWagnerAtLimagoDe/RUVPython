from Clients.GameClient import Spieler
from Games.TakeGameModul import TakeGame

game = TakeGame()
client = Spieler(game)

client.run()

