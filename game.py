from player import Player
import pygame

class Game:
    def __init__(self):
        self.player = Player("assets/red_tank.png", 200, 200)
        self.player2 = Player("assets/bleu_tank.png", 600, 200)

        self.pressed = {}

