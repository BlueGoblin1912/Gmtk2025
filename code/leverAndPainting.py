import pygame

class Lever(pygame.sprite.Sprite):
    def __init__(self, pos, groups,activeMethod):
        super().__init__(groups)
        self.status = "unactive"
        self.usable = True
        self.image = pygame.image.load(f"../graphics/sprites/leveroff.png")
        self.image = pygame.transform.scale_by(self.image,4)
        pos = (pos[0]-32,pos[1]-12)
        self.rect = self.image.get_rect(topleft = pos)
        # self.rect.inflate_ip(20,20)
        #the method which is called when the lever is active
        self.activeMethod = activeMethod
        
    def toggleActivation(self):
        '''toggles the state of the interactive object between on and off'''
        if self.status == "active":
            self.status = "leveroff"
            self.usable = True
        elif self.status == "unactive":
            self.status = "leveron"
        self.image = pygame.image.load(f"../graphics/sprites/{self.status}.png").convert_alpha()

    def checkActive(self):
        '''checks if the sprite is able to its ability
        uses it if it meets the requirements'''
        if self.status == "active" and self.usable:
            self.activeMethod()
            self.usable = False
    
    def update(self):
        self.checkActive()

class Painting(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../graphics/sprites/painting.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)