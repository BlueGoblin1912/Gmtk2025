import pygame

class Pit(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)

class Safe(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)
