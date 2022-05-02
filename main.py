import pygame 
from game import Game
from gpiozero import Button
pygame.init()


pygame.display.set_caption("Test")
screen = pygame.display.set_mode((800,480))



backgroound = pygame.image.load("assets/Clipboard01.jpg")

game = Game()
running = True




button1red = Button("GPIO15")
button2red = Button("GPIO18")
button1blue = Button("GPIO12")
button2blue = Button("GPIO07")

joystickBlueUp = Button("GPIO11")
joystickBlueLeft =Button("GPIO06")
joystickBlueRight = Button("GPIO13")
joystickBlueDown = Button("GPIO05")

joystickRedUp = Button("GPIO04")
joystickRedLeft =Button("GPIO27")
joystickRedRight = Button("GPIO22")
joystickRedDown = Button("GPIO17")




while running:
 
    
    # joystickBlueUp.when_pressed = JoystickUp
    # joystickBlueLeft.when_pressed = JoystickLeft
    # joystickBlueRight.when_pressed = JoystickRight
    # joystickBlueDown.when_pressed =JoystickDown
    
    # joystickRedUp.when_pressed = JoystickUp
    # joystickRedLeft.when_pressed = JoystickLeft
    # joystickRedRight.when_pressed = JoystickRight
    # joystickRedDown.when_pressed =JoystickDown
    
    # button1red.when_pressed = ButtonOn
    # button1red.when_released = ButtonOff

    # button2red.when_pressed = ButtonOn
    # button2red.when_released = ButtonOff

    # button1blue.when_pressed = ButtonOn
    # button1blue.when_released = ButtonOff

    # button2blue.when_pressed = ButtonOn
    # button2blue.when_released = ButtonOff

    screen.blit(backgroound,(0,0))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)

    if game.pressed.get(joystickBlueRight) and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()
    elif game.pressed.get(joystickBlueLeft) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(joystickBlueUp) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(joystickBlueDown) and game.player.rect.y < screen.get_height() - game.player.rect.height:
        game.player.move_down()
        

    print(game.player.rect.x)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
          