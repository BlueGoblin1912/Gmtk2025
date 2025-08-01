import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, pos, groups,player):
        super().__init__(groups)
        
        self.image = pygame.image.load("../graphics/sprites/spike/off.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.image.get_rect()

        self.player = player

    def collision(self):
        if self.rect.colliderect(self.player.hitbox):
            self.image = pygame.image.load("../graphics/sprites/spike/on.png").convert_alpha()
            self.image = pygame.transform.scale2x(self.image)
            

    def update(self):
        self.collision()