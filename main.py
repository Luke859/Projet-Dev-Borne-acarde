import pygame 
from game import Game
from gpiozero import Button
pygame.init()

pygame.display.set_caption("Test")
screen = pygame.display.set_mode((800,400))

backgroound = pygame.image.load("assets/Clipboard01.jpg")

banner = pygame.image.load("assets/tankImage.png")
banner = pygame.transform.scale(banner, (250, 250))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4 

game = Game()
running = True

# def ButtonOn(button):
#     print("button " + str(button.pin) + " pressed")

# def ButtonOff(button):
#     print("button " + str(button.pin) + " OFF")
    
# def JoystickUp(joystick):
#     print("Joystick UP " + str(joystick.pin))
    
# def JoystickLeft(joystick):
#     print("Joystick LEFT " + str(joystick.pin))
    
# def JoystickRight(joystick):
#     print("Joystick RIGHT " + str(joystick.pin))
    
# def JoystickDown(joystick):
#     print("Joystick DOWN " + str(joystick.pin))

while running:

    screen.blit(backgroound,(0,0))

    if game.is_playing:
        game.update(screen)

    else:
        screen.blit(banner, banner_rect)


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
          