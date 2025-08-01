import pygame
from player import Player
from support import *
from barrier import *
from door import Door
from chest import Chest
from leverAndPainting import *
from spike import Spike
from button import Button
from shooter import Shooter
from settings import *

class Level:
    def __init__(self,screen):
        self.screen = screen
        self.level = "room 1"
        

        #groups
        self.visibleSprites = YSortCameraGroup()
        self.collisionSprites = pygame.sprite.Group()
        self.interactiveSprites = pygame.sprite.Group()
        self.harmSprites = pygame.sprite.Group()
        self.doorSprites = pygame.sprite.Group()
        self.worldSprites = pygame.sprite.Group()

        self.playerPos = (330,490)
        self.player = Player(self.playerPos,[self.visibleSprites],self.changeRoom)

        self.createLevel(self.level)

    def createLevel(self,level):
        CSVs = {"invisible":import_csv_layout(f"../graphics/map/levels/{level}/csv/{level}_invisible.csv"),
                "objects":import_csv_layout(f"../graphics/map/levels/{level}/csv/{level}_objects.csv")}
        
        for type, csv in CSVs.items():
            for rowIndex,row in enumerate(csv):
                for colIndex,col in enumerate(row):
                    if col != "-1":
                        x = colIndex * 64
                        y = rowIndex * 64
                        if type == "invisible":
                            if col == "0":
                                Barrier((x,y),[self.collisionSprites,self.worldSprites])
                        if type == "objects":
                            if col == "0":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorup.png","up","closed")
                                print((x,y))
                            if col == "1":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorright.png","right","closed")
                                print((x,y))
                            if col == "2":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorleft.png","left","closed")
                                print((x,y))
                            if col == "3":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doordown.png","down","closed")
                                print((x,y))
                            if col == "4":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorlocked.png","up","locked")
                                print((x,y))
                            if col == "5":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door1.png","up","closed")
                                print((x,y))
                            if col == "6":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door2.png","up","trapped")
                                print((x,y))
                            if col == "7":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door3.png","up","trapped")
                                print((x,y))
                            if col == "22":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorleft.png","left","locked")
                                print((x,y))
                            if col == "8":
                                Table((x,y),[self.visibleSprites,self.collisionSprites,self.worldSprites])
                            if col == "9":
                                Chair((x,y),[self.visibleSprites,self.collisionSprites,self.worldSprites])
                            if col == "10":
                                Chest((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"closed",self.level)
                            if col == "11":
                                Chest((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"trapped",self.level)
                            if col == "12":
                                Lever((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"lights")
                            if col == "13":
                                Painting((x,y-128),[self.visibleSprites,self.worldSprites])
                            if col == "14":
                                Spike((x,y-64),[self.visibleSprites,self.harmSprites,self.worldSprites])
                            if col == "15":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"psi")
                            if col == "16":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"omega")
                            if col == "17":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"pi")
                            if col == "18":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"phi")
                            if col == "19":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"xi")
                            if col == "20":
                                Shooter((x,y),[self.visibleSprites,self.worldSprites],"left")
                            if col == "21":
                                Shooter((x,y),[self.visibleSprites,self.worldSprites],"right")

    def changeRoom(self):
        for sprite in self.doorSprites:
            if sprite.rect.colliderect(self.player.rect):
                level = doorDests[self.level][sprite.rect.topleft]["room"]
                coords = doorDests[self.level][sprite.rect.topleft]["coords"]
                self.player.rect.topleft = coords
                self.level = level
                for sprite in self.worldSprites: sprite.kill()
                self.createLevel(self.level)

    def run(self):
        self.player.update()

    def update(self):
        self.visibleSprites.custom_draw(self.player,self.level)
        self.run()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self,):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player,level):
        self.floor_surf = pygame.image.load(f'../graphics/map/levels/{level}/csv/{level}.png').convert_alpha()
        self.floor_surf = pygame.transform.scale_by(self.floor_surf,2)
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

        self.display_surface.fill("#000000")
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
