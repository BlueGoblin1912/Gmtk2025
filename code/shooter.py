import pygame

class Shooter(pygame.sprite.Sprite):
    def __init__(self, pos, groups, direction):
        super().__init__(groups)
        self.image = pygame.image.load(f"../graphics/sprites/{direction}shooter.png")
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)