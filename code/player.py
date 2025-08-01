import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,changeRoom,obsticleSprites):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-50)

        self.direction = pygame.math.Vector2()
        
        self.obsticleSprites = obsticleSprites

        self.stats = {"health":100,"speed":5}

        self.changeRoom = changeRoom
        self.canChange = True
        self.changeTime = 0
    
    def collide(self,direction):
        '''checks for entity collision with the boarder sprites
        if the front side of the rect is colliding with another rect then
        it get placed at the boundary of the two rects'''
        if direction == "horizontal":
            for sprite in self.obsticleSprites:
                #moving right
                if self.direction.x > 0:
                    if sprite.rect.colliderect(self.hitbox):
                        self.hitbox.right = sprite.rect.left
                #moving left
                elif self.direction.x < 0:
                    if sprite.rect.colliderect(self.hitbox):
                        self.hitbox.left = sprite.rect.right

        elif direction == "vertical":
            for sprite in self.obsticleSprites:
                #moving down
                if self.direction.y > 0:

                    if sprite.rect.colliderect(self.hitbox):   
                        self.hitbox.bottom = sprite.rect.top

                #moving up
                elif self.direction.y < 0:
                    if sprite.rect.colliderect(self.hitbox):
                        self.hitbox.top = sprite.rect.bottom



    
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * self.stats["speed"]
        self.collide("horizontal")
        self.hitbox.y += self.direction.y * self.stats["speed"]
        self.collide("vertical")
        self.direction = pygame.math.Vector2()
        self.rect.center = self.hitbox.center

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y += -1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x += -1
        if keys[pygame.K_d]:
            self.direction.x += 1

        if keys[pygame.K_e]:
            if self.canChange:
                self.canChange = False
                self.changeTime = pygame.time.get_ticks()
                self.changeRoom()
                


    def cooldowns(self):
        currentTime = pygame.time.get_ticks()

        if currentTime - self.changeTime >= 200:
            self.canChange = True


    def update(self):
        self.input()
        self.move()
        self.cooldowns()