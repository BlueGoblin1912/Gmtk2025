import pygame
from settings import *

class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, groups, status, room,player):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/chest.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        pos = (pos[0],pos[1]-64)
        self.rect = self.image.get_rect(topleft = pos)
        self.player = player

        self.status = status
        
        self.loot = lootTable[room]
        self.lootImage = f"../graphics/sprites/{self.loot}.png"
    
    def activate(self):
        if self.status == "trapped":
            self.player.health = 0
        elif self.status == "closed" and self.lootImage not in self.player.inventory:
            self.status = "open"
            for index,item in enumerate(self.player.inventory):
                if item == None:
                    self.player.inventory[index] = self.lootImage
                    break



        