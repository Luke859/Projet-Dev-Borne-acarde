import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player =player
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (30,50))
        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x 
        
        self.rect.y = player.rect.y 
        self.velocity = 10
        

    def remove(self):
        self.player.all_projectiles.remove(self)
        
    def move(self, direction):
        self.rect.x += self.velocity * direction
     


        if self.rect.x > 800:
            self.remove()


