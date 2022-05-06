import pygame 
import math
from game import Game
from gpiozero import Button
pygame.init()

pygame.display.set_caption("Test")
screen = pygame.display.set_mode((800,400))

background = pygame.image.load("assets/Clipboard01.jpg")

# button1blue = Button("GPIO12")

banner = pygame.image.load("assets/tankImage.png")
banner = pygame.transform.scale(banner, (200, 200))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()
running = True

while running:

    screen.blit(background,(0,0))

    if game.is_playing:
        game.update(screen)

    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        # if event.type == button1blue.is_pressed :
        #     if play_button_rect.collidepoint(event.pos):
        #         game.is_playing = True 