import pygame
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


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 140, 140)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('->', 25, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.currentName = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.htpx, self.htpy = self.mid_w, self.mid_h + 110
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text("Play", 30, self.startx, self.starty)
            self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
            self.game.draw_text("How to play", 30, self.htpx, self.htpy)
            self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if joystickBlueDown.is_pressed or joystickRedDown.is_pressed:
            if self.currentName == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.currentName = 'Options'
            elif self.currentName == 'Options':
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.currentName = 'How to play'
            elif self.currentName == 'How to play':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.currentName = 'Credits'
            elif self.currentName == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.currentName = 'Start'
        elif  joystickBlueUp.is_pressed or joystickRedUp.is_pressed :
            if self.currentName == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.currentName = 'Credits'
            elif self.currentName == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.currentName = 'Start'
            elif self.currentName == 'How to play':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.currentName = 'Options'
            elif self.currentName == 'Credits':
                self.cursor_rect.midtop = (self.htpx + self.offset, self.htpy)
                self.currentName = 'How to play'

    def check_input(self):
        self.move_cursor()
        if button1red.is_pressed or button1blue.is_pressed:
            if self.currentName == 'Start':
                self.game.playing = True
            elif self.currentName == 'Options':
                self.game.curr_menu = self.game.options
            elif self.currentName == 'How to play':
                self.game.curr_menu = self.game.htp
            elif self.currentName == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if button1red.is_pressed or button1blue.is_pressed:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif button1red.is_pressed or button1blue.is_pressed:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('Jeu cree par', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 0)
            self.game.draw_text('Nathy Mellal & Luke Jones', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('en B2 Informatique a Ynov Campus', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.blit_screen()

class HTPMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('how to play', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.imageJoystick = pygame.image.load("assets/joystick.jpg")
            self.rect = self.imageJoystick.get_rect()
            self.rect.x = 500
            self.rect.y = 300
            self.blit_screen() 