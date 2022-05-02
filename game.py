from player import Player

class Game:
    def __init__(self):
        self.player = Player("assets/red_tank.png", 100, 100)
        self.player2 = Player("assets/blue_tank.png", 800, 600)
        self.pressed = {}

