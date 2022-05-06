import pygame 
from game import Game
pygame.init()

game = Game()
running = True

while running:
    
    game.curr_menu.display_menu()
    game.game_loop()
        
    print(game.player.rect.x)
    

    pygame.display.flip()

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    #         pygame.quit()
    #     elif event.type == pygame.KEYDOWN:
    #         game.pressed[event.key] = True

    #         if button2blue.is_pressed :
    #             game.player.launch_projectile()

    #     elif event.type == pygame.KEYUP:
    #         game.pressed[event.key] = False
          