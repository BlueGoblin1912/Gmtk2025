import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self,pos, groups,direction):
        super().__init__(groups)
        self.image = pygame.image.load(f"../graphics/sprites/fireball{direction}.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = pos)
        self.direction = direction
        self.speed = 10
        self.damage = 25

        if self.direction == "left":
            self.speed = -self.speed

    def move(self):
        self.rect.centerx += self.speed

    def checkDeath(self,player,collisionSprites):
        if self.rect.colliderect(player.rect) and player.canTakeDamage:
            player.health -= self.damage
            player.canTakeDamage = False
            player.damageTime = pygame.time.get_ticks()
            self.kill()
        for sprite in collisionSprites:
            if self.rect.colliderect(sprite.rect):
                self.kill()
    
    
    def update(self,player,collisionSprites):
        self.move()
        self.checkDeath(player,collisionSprites)

