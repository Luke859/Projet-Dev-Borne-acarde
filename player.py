from operator import imod
import pygame
from projectile import Projectile
class Player(pygame.sprite.Sprite):


    def __init__(self, sprite, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 7
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
        
    def move_up(self):
        self.rect.y -= self.velocity
        
    def move_down(self):
        self.rect.y += self.velocity