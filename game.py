from player import Player
from menu import *
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        # self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800,400
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'Nuvel.ttf'

        self.all_players = pygame.sprite.Group()
        self.player = Player("assets/red_tank.png", 200, 200)
        self.player2 = Player("assets/bleu_tank.png", 600, 200)
        self.all_players.add(self.player)
        self.all_players.add(self.player2)

        # self.playerToucher = pygame.USEREVENT + 1
        # self.player2Toucher = pygame.USEREVENT + 2

        self.background = pygame.image.load("assets/Clipboard01.jpg")
        self.border = pygame.Rect(self.DISPLAY_W/2 - 5, 0, 10, self.DISPLAY_H)
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.pressed = {}
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.htp = HTPMenu(self)
        self.curr_menu = self.main_menu

    def game_time(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.window.blit(self.background,(0,0))
            self.window.blit(self.player.image, self.player.rect)
            self.window.blit(self.player2.image, self.player2.rect)
            pygame.draw.rect(self.window, self.BLACK, self.border)
            
            for projectile in self.player.all_projectiles:
                projectile.move(1)
                # if self.player2.check_collision(projectile): 
                #     pygame.event.post(pygame.event.Event(self.player2Toucher))
                #     self.player.all_projectiles.remove(projectile)
                
            self.player.all_projectiles.draw(self.window)

            if joystickBlueRight.is_pressed and self.player.rect.x + self.player.rect.width < self.border.x:
                self.player.move_right()
            elif joystickBlueLeft.is_pressed and self.player.rect.x > 0:
                self.player.move_left()
            elif joystickBlueUp.is_pressed and self.player.rect.y > 0:
                self.player.move_up()
            elif joystickBlueDown.is_pressed and self.player.rect.y < self.window.get_height() - self.player.rect.height:
                self.player.move_down()
            if button2blue.is_pressed :
                self.player.launch_projectile()

            
            for projectile in self.player2.all_projectiles:
                projectile.move(-1)
                # if self.player.check_collision(projectile): 
                #     pygame.event.post(pygame.event.Event(self.playerToucher))
                #     self.player2.all_projectiles.remove(projectile)

            self.player2.all_projectiles.draw(self.window)

            if joystickRedRight.is_pressed and self.player2.rect.x < self.window.get_width() - self.player2.rect.width:
                self.player2.move_right()
            elif joystickRedLeft.is_pressed and self.player2.rect.x > self.border.x + self.border.width :
                self.player2.move_left()
            elif joystickRedUp.is_pressed and self.player2.rect.y > 0:
                self.player2.move_up()
            elif joystickRedDown.is_pressed and self.player2.rect.y < self.window.get_height() - self.player2.rect.height:
                self.player2.move_down()
            if button2red.is_pressed :
                self.player2.launch_projectile()
            pygame.display.update()
            self.reset_keys()

    # def check_collision(self, sprite, group):
    #     return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RETURN:
            #         self.START_KEY = True
            #     if event.key == pygame.K_BACKSPACE:
            #         self.BACK_KEY = True
            #     if event.key == pygame.K_DOWN:
            #         self.DOWN_KEY = True
            #     if event.key == pygame.K_UP:
            #         self.UP_KEY = True

    # def reset_keys(self):
    #     self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)


