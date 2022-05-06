from player import Player
from gpiozero import Button

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player("assets/red_tank.png", 200, 200) 
        self.player2 = Player("assets/bleu_tank.png", 600, 200)
        self.pressed = {}
