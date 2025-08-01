import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type):
        super().__init__(groups)
        self.image = pygame.image.load(f"../graphics/sprites/symbols/{type}.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.type = type