import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
         
        self.image = pygame.image.load("../graphics/sprites/spike/off.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30,-50)
        self.status = "inactive"

    def DamageCollision(self,player):
        if self.hitbox.colliderect(player.rect) and player.canTakeDamage and self.status == "inactive":
            self.image = pygame.image.load("../graphics/sprites/spike/on.png").convert_alpha()
            self.image = pygame.transform.scale2x(self.image)
            self.status = "active"
            player.health -= 33
            player.canTakeDamage = False
            player.damageTime = pygame.time.get_ticks()

    def collide(self,player,group):
        if self.status == "active":
            group.add(self)

    def update(self,player,group):
        self.DamageCollision(player)
        self.collide(player,group)