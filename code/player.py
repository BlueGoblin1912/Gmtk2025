import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,changeRoom):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.changeRoom = changeRoom

        self.stats = {"health":100,"speed":5}

        self.canChange = True
        self.changeTime = 0

    
    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * self.stats["speed"]
        self.rect.y += self.direction.y * self.stats["speed"]
        self.direction = pygame.math.Vector2()

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