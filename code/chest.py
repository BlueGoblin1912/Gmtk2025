import pygame
from settings import *

class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, groups, status, room):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/chest.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        pos = (pos[0],pos[1]-64)
        self.rect = self.image.get_rect(topleft = pos)

        self.status = status
        
        self.loot = lootTable[room]