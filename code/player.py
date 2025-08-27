import pygame
from settings import *
from math import sin

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,changeRoom,obsticleSprites,interact,useItem):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-50)
        self.hitbox2 = self.rect.inflate(0,-20)
        self.direction = pygame.math.Vector2()
        
        self.text = pygame.font.Font(font)

        self.obsticleSprites = obsticleSprites

        self.stats = {"health":100,"speed":5}
        self.health = self.stats["health"]

        self.changeRoom = changeRoom
        self.interact = interact
        self.useItem = useItem

        self.idolUsed = False
        self.idolPos = (0,0)

        self.canChange = True
        self.changeTime = 0

        self.canCombo = True
        self.comboTime = 0

        self.canTakeDamage = True
        self.damageTime = 0

        self.inventory = [None,None,None,None]
        self.combo = []

        self.path = ()

    def damageAnimation(self):
        if not self.canTakeDamage:
            value = sin(pygame.time.get_ticks())
            if value >= 0:
                alpha = 255
            else:
                alpha = 0
            
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
    def collide(self,direction,sprites):
        '''checks for entity collision with the boarder sprites
        if the front side of the rect is colliding with another rect then
        it get placed at the boundary of the two rects'''
        if direction == "horizontal":
            for sprite in sprites:
                #moving right
                if self.direction.x > 0:
                    if sprite.rect.colliderect(self.hitbox):
                        self.hitbox.right = sprite.rect.left
                #moving left
                elif self.direction.x < 0:
                    if sprite.rect.colliderect(self.hitbox):
                        self.hitbox.left = sprite.rect.right

        elif direction == "vertical":
            for sprite in sprites:
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
        self.collide("horizontal", self.obsticleSprites)
        self.hitbox.y += self.direction.y * self.stats["speed"]
        self.collide("vertical", self.obsticleSprites)
        self.rect.center = self.hitbox.center
        self.hitbox2.center = self.hitbox.center

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction = pygame.math.Vector2()
        if keys[pygame.K_w]:
            self.direction.y += -1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x += -1
        if keys[pygame.K_d]:
            self.direction.x += 1

        if keys[pygame.K_e]:
            self.interact()
            if self.canChange:
                self.canChange = False
                self.changeTime = pygame.time.get_ticks()
                self.changeRoom()
        
        if keys[pygame.K_1]:
            self.useItem(0)
        if keys[pygame.K_2]:
            self.useItem(1)
        if keys[pygame.K_3]:
            self.useItem(2)
        if keys[pygame.K_4]:
            self.useItem(3)
                            
    def displayIdol(self):
        if self.idolUsed:
            screen = pygame.display.get_surface()
            surf = pygame.transform.scale_by(pygame.image.load("../graphics/sprites/idol.png").convert_alpha(),3.5)
            rect = surf.get_rect(center = (340,735))
            room = self.text.render(f"{self.idolPos}",False,"#aaaaaa")
            roomRect = room.get_rect(center = (340,770))
            screen.blit(room,roomRect)
            screen.blit(surf,rect)

    def cooldowns(self):
        currentTime = pygame.time.get_ticks()

        if currentTime - self.changeTime >= 200:
            self.canChange = True

        if  currentTime - self.damageTime >= 500:
            self.canTakeDamage = True
        
        if currentTime - self.comboTime >= 200:
            self.canCombo = True

    def pathTaken(self,room,sprites):
        if room == "room 4":
            for sprite in sprites:
                if self.hitbox.colliderect(sprite.rect):
                    self.path = sprite.rect.center

    def update(self,room,sprites):
        self.input()
        self.move()
        self.damageAnimation()
        self.pathTaken(room,sprites)
        self.cooldowns()
        self.displayIdol()