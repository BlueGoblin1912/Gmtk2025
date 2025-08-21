import pygame
import random

class Shooter(pygame.sprite.Sprite):
    def __init__(self, pos, groups, direction):
        super().__init__(groups)
        self.image = pygame.image.load(f"../graphics/sprites/{direction}shooter.png")
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        #shooting stuff
        self.direction = direction
        self.canShoot = True
        self.shotTime = 0
        self.fireBalls = pygame.sprite.Group()


    def timeShots(self,shoot):
        delay = random.randint(700,1000)
        currentTime = pygame.time.get_ticks()
        if currentTime - self.shotTime >= delay:
            self.canShoot = True

        if self.canShoot:
            self.canShoot = False
            self.shotTime = pygame.time.get_ticks()
            shoot(self.rect.center,self.direction)
            
    def update(self,shoot):
        self.timeShots(shoot)