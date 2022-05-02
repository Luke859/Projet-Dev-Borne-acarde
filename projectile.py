import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player =player
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x 
        self.rect.y = player.rect.y 
        self.velocity = 2

    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self):
        self.rect.x += self.velocity

        if self.rect.x > 800:
            self.remove()
