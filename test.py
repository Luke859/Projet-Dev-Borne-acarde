import pygame
import os 
from gpiozero import Button

LUKEEEEEEEEEEEEEEEEEEEE

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

pygame.init()

display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Borne d'arcade")
RED = (255, 0, 0)
FPS = 60 
CHARACTER_WIDTH, CHARACTER_HEIGHT =  120, 100

#CHARACTER 1
CHARACTER1_IMAGE = pygame.image.load(os.path.join('images', 'ninja.png'))
CHARACTER1 = pygame.transform.scale(CHARACTER1_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

#CHARACTER 2
CHARACTER2_IMAGE = pygame.image.load(os.path.join('images', 'pacman.png'))
CHARACTER2 = pygame.transform.scale(CHARACTER2_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

#Style d notre jeu
def window_style(character1, character2):
    display.fill(RED)
    display.blit(CHARACTER1, (character1.x, character1.y)) 
    display.blit(CHARACTER2, (character2.x, character2.y)) 
    pygame.display.update()

#Page de notre jeu
def main():
    character1 = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    character2 = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()  #Controller la vitesse d'affichage de notre boucle 
    
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


    open = True
    while open:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                open = False

        character1.x += 1
        character2.x -= 1

        window_style(character1, character2)
    pygame.quit()

if __name__ == '__main__':
    main()