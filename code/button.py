import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, groups,player, type):
        super().__init__(groups)
        self.image = pygame.image.load(f"../graphics/sprites/symbols/{type}.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.player = player
        self.type = type
    
    def reset(self):
        self.image = pygame.image.load(f"../graphics/sprites/symbols/{self.type}.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)

    def activate(self):
        if self.player.canCombo:
            self.player.canCombo = False
            self.player.comboTime = pygame.time.get_ticks()
            self.player.combo.append(self.type)
            self.image = pygame.image.load(f"../graphics/sprites/symbols/{self.type} on.png").convert_alpha()
            self.image = pygame.transform.scale2x(self.image)