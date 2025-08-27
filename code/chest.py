import pygame
from settings import *

class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, groups, status, room, player, usedChests):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/chest.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        pos = (pos[0],pos[1]-64)
        self.rect = self.image.get_rect(topleft = pos)
        self.player = player

        self.status = status
        self.usedChests = usedChests
        self.room = room
        
        self.loot = lootTable[self.room]
        self.lootImage = f"../graphics/sprites/{self.loot}.png"

        if room in self.usedChests:
            self.status = "open"
            self.image = pygame.image.load("../graphics/sprites/chestopen.png").convert_alpha()
            self.image = pygame.transform.scale2x(self.image)
    
    def activate(self):
        if self.room not in self.usedChests:
            if self.status == "trapped":
                self.status = "open"
                self.image = pygame.image.load("../graphics/sprites/chestopen.png").convert_alpha()
                self.usedChests.append(self.room)
                self.image = pygame.transform.scale2x(self.image)
                self.player.canTakeDamage = False
                self.player.damageTime = pygame.time.get_ticks()
                self.player.health -= 75
            elif self.status == "closed":
                self.status = "open"
                self.image = pygame.image.load("../graphics/sprites/chestopen.png").convert_alpha()
                self.usedChests.append(self.room)
                self.image = pygame.transform.scale2x(self.image)
                if self.lootImage not in self.player.inventory:
                    for index,item in enumerate(self.player.inventory):
                        if item == None:
                            self.player.inventory[index] = self.lootImage
                            break