from player import Player
from gpiozero import Button

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

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player("assets/red_tank.png", 200, 200) 
        self.player2 = Player("assets/bleu_tank.png", 600, 200)
        self.pressed = {}

    def update(self, screen): 
        screen.blit(self.player.image, self.player.rect)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        if joystickBlueRight.is_pressed and self.player.rect.x < screen.get_width() - game.player.rect.width:
            self.player.move_right()
        elif joystickBlueLeft.is_pressed and self.player.rect.x > 0:
            self.player.move_left()
        elif joystickBlueUp.is_pressed and self.player.rect.y > 0:
            self.player.move_up()
        elif joystickBlueDown.is_pressed and self.player.rect.y < screen.get_height() - game.player.rect.height:
            self.player.move_down()
        if button2blue.is_pressed :
            self.player.launch_projectile()
