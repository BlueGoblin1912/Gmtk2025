import pygame

class Alter(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/alter.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)

    def active(self):
        self.image = pygame.image.load("../graphics/sprites/alter on.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)