import pygame 
from game import Game
from gpiozero import Button
pygame.init()

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

pygame.display.set_caption("Test")
screen = pygame.display.set_mode((800,400))



backgroound = pygame.image.load("assets/Clipboard01.jpg")

game = Game()
running = True


def ButtonOn(button):
    print("button " + str(button.pin) + " pressed")

def ButtonOff(button):
    print("button " + str(button.pin) + " OFF")
    
def JoystickUp(joystick):
    print("Joystick UP " + str(joystick.pin))
    
def JoystickLeft(joystick):
    print("Joystick LEFT " + str(joystick.pin))
    
def JoystickRight(joystick):
    print("Joystick RIGHT " + str(joystick.pin))
    
def JoystickDown(joystick):
    print("Joystick DOWN " + str(joystick.pin))


while running:
 
    
    joystickBlueUp.when_pressed = JoystickUp
    joystickBlueLeft.when_pressed = JoystickLeft
    joystickBlueRight.when_pressed = JoystickRight
    joystickBlueDown.when_pressed =JoystickDown
    
    joystickRedUp.when_pressed = JoystickUp
    joystickRedLeft.when_pressed = JoystickLeft
    joystickRedRight.when_pressed = JoystickRight
    joystickRedDown.when_pressed =JoystickDown
    
    button1red.when_pressed = ButtonOn
    button1red.when_released = ButtonOff

    button2red.when_pressed = ButtonOn
    button2red.when_released = ButtonOff

    button1blue.when_pressed = ButtonOn
    button1blue.when_released = ButtonOff

    button2blue.when_pressed = ButtonOn
    button2blue.when_released = ButtonOff

    screen.blit(backgroound,(0,0))

    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.player2.image, game.player2.rect)

    for projectile in game.player.all_projectiles:
        projectile.move(1)

    game.player.all_projectiles.draw(screen)

    if joystickBlueRight.is_pressed and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()
    elif joystickBlueLeft.is_pressed and game.player.rect.x > 0:
        game.player.move_left()
    elif joystickBlueUp.is_pressed and game.player.rect.y > 0:
        game.player.move_up()
    elif joystickBlueDown.is_pressed and game.player.rect.y < screen.get_height() - game.player.rect.height:
        game.player.move_down()
    if button2blue.is_pressed :
        game.player.launch_projectile()

    
    for projectile in game.player2.all_projectiles:
        projectile.move(-1)

        game.player2.all_projectiles.draw(screen)

    if joystickRedRight.is_pressed and game.player2.rect.x < screen.get_width() - game.player2.rect.width:
        game.player2.move_right()
    elif joystickRedLeft.is_pressed and game.player2.rect.x > 0:
        game.player2.move_left()
    elif joystickRedUp.is_pressed and game.player2.rect.y > 0:
        game.player2.move_up()
    elif joystickRedDown.is_pressed and game.player2.rect.y < screen.get_height() - game.player2.rect.height:
        game.player2.move_down()
    if button2red.is_pressed :
        game.player2.launch_projectile()
        

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
          