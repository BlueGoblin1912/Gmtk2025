import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/portal.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)

    