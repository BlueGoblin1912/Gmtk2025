import pygame

class Lever(pygame.sprite.Sprite):
    def __init__(self, pos, groups,activeMethod):
        super().__init__(groups)
        self.status = "leveroff"
        self.usable = True
        self.image = pygame.image.load(f"../graphics/sprites/leveroff.png")
        self.image = pygame.transform.scale_by(self.image,4)

        pos = (pos[0]-32,pos[1]-12)
        self.rect = self.image.get_rect(topleft = pos)

        self.activeMethod = activeMethod

    def activate(self):
        if self.status == "leveroff":
            self.status = "leveron"
        self.activeMethod()
        self.image = pygame.image.load(f"../graphics/sprites/{self.status}.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,4)

class Painting(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/painting.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)

    def activate(self):
        self.rect.left -= 128