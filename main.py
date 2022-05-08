import pygame 
from game import Game
pygame.init()

game = Game()
running = True

while running:
    
    game.curr_menu.display_menu()
    game.game()
    
    pygame.display.flip()
          