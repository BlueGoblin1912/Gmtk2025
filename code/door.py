import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self,pos,groups,path,direction,status,):
        super().__init__(groups)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = direction
        self.status = status