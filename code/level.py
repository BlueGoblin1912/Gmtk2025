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
from wall import Wall
from portal import Portal
from alter import Alter
from pit import *
from ball import Ball

class Level:
    def __init__(self,screen):
        self.screen = screen
        self.level = "room 1"
        self.startLevel = "room 1"
        self.startTime = pygame.time.get_ticks()

        self.minutes = 1
        self.seconds = 30
        self.lastsecond = 0
        self.offsetTime = 0
        self.sleepPercent = 0
        pygame.font.init()
        self.textFont = pygame.font.Font(font,30)

        #groups
        self.visibleSprites = YSortCameraGroup()
        self.collisionSprites = pygame.sprite.Group()
        self.interactiveSprites = pygame.sprite.Group()
        self.harmSprites = pygame.sprite.Group()
        self.doorSprites = pygame.sprite.Group()
        self.worldSprites = pygame.sprite.Group()
        self.trapSprites = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.exit = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.alter = pygame.sprite.Group()
        self.pitSprites = pygame.sprite.Group()
        self.safeSprites = pygame.sprite.Group()
        self.shooterSprites = pygame.sprite.Group()

        self.portalOn = False
        self.lightsOff = False
        self.playerPos = (330,490)
        self.player = Player(self.playerPos,[self.visibleSprites],self.changeRoom,self.collisionSprites,self.interact,self.useItem)
        

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
                            elif col == "3":
                                Pit((x,y),[self.pitSprites,self.worldSprites])
                            elif col == "1":
                                Safe((x,y),[self.safeSprites,self.worldSprites])
                        elif type == "objects":
                            if col == "0":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorup.png","up","closed")
                            elif col == "1":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorright.png","right","closed")
                            elif col == "2":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorleft.png","left","closed")
                            elif col == "3":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doordown.png","down","closed")
                            elif col == "4":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/doorlocked.png","up","locked")
                            elif col == "5":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door1.png","up","closed")
                            elif col == "6":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door2.png","up","trapped")
                            elif col == "7":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites],
                                     "../graphics/sprites/doors/door3.png","up","trapped")
                            elif col == "22":
                                Door((x,y),[self.visibleSprites,self.doorSprites,self.worldSprites,self.exit],
                                     "../graphics/sprites/doors/doorleft.png","left","locked")
                            elif col == "8":
                                Table((x,y),[self.visibleSprites,self.collisionSprites,self.worldSprites])
                            elif col == "9":
                                Chair((x,y),[self.visibleSprites,self.collisionSprites,self.worldSprites])
                            elif col == "10":
                                Chest((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"closed",self.level,self.player)
                            elif col == "11":
                                Chest((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],"trapped",self.level,self.player)
                            elif col == "12":
                                Lever((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites],self.turnOffTheLights)
                            elif col == "13":
                                Painting((x,y-128),[self.visibleSprites,self.worldSprites,self.interactiveSprites])
                            elif col == "14":
                                Spike((x,y-22),[self.visibleSprites,self.worldSprites,self.trapSprites])
                            elif col == "15":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites,self.buttons],self.player,"psi")
                            elif col == "16":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites,self.buttons],self.player,"omega")
                            elif col == "17":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites,self.buttons],self.player,"pi")
                            elif col == "18":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites,self.buttons],self.player,"phi")
                            elif col == "19":
                                Button((x,y),[self.visibleSprites,self.interactiveSprites,self.worldSprites,self.buttons],self.player,"xi")
                            elif col == "20":
                                Shooter((x,y),[self.visibleSprites,self.worldSprites,self.shooterSprites],"right")
                            elif col == "21":
                                Shooter((x,y),[self.visibleSprites,self.worldSprites,self.shooterSprites],"left")
                            elif col == "23":
                                Wall((x,y),[self.visibleSprites,self.collisionSprites,self.worldSprites])
                            elif col == "24":
                                Portal((x,y-64),[self.visibleSprites,self.collisionSprites,self.worldSprites,self.portal])
                            elif col == "25":
                                Alter((x,y-32),[self.visibleSprites,self.collisionSprites,self.worldSprites,self.alter])

    def turnOffTheLights(self):
        self.lightsOff = True
        self.visibleSprites.turnOffTheLights()

    def showBar(self,top,current,max,colour):
        rect = pygame.Rect(10,top,200,25)
        pygame.draw.rect(self.screen,"#222222",rect)

        ratio = current / max
        current_width = rect.width * ratio
        current_rect = rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.screen,colour,current_rect)
        pygame.draw.rect(self.screen,"#111111",rect,3)

    def timer(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastsecond >=1000:
            self.lastsecond = pygame.time.get_ticks()
            self.seconds -= 1
            if self.seconds < 0:
                self.minutes -= 1
                self.seconds = 59
        if self.minutes < 0:
            self.sleepPercent += 1/3
            
        if self.offsetTime != 0:
            self.seconds += self.offsetTime
            if self.seconds >= 60:
                self.seconds -= 60
                self.minutes += 1
            self.offsetTime = 0

        if self.minutes < 0:
            if self.sleepPercent > 100:
                self.restart()
            else:
                self.showBar(45,self.sleepPercent,100,"#8c00ff")
            
        else:
            text = self.textFont.render(f"{self.minutes}:{self.seconds} Remaining",False,"#86000088")
            rect = text.get_rect(center = (SCREENWIDTH//2,20))
            textBg = self.textFont.render(f"{self.minutes}:{self.seconds} Remaining",False,"#47000088")
            rectBg = text.get_rect(center = (SCREENWIDTH//2+4,24))
            self.screen.blit(textBg,rectBg)
            self.screen.blit(text,rect)

    def restart(self):
        self.minutes = 1
        self.seconds = 30
        self.lastsecond = 0
        self.offsetTime = 0
        self.sleepPercent = 0

        self.level = self.startLevel
        self.player.hitbox.topleft = self.playerPos
        self.playerPos=(330,490)
        #self.player.inventory = [None,None,None,None]
        self.player.idolUsed = False
        self.player.combo = []
        self.player.health = self.player.stats["health"]
        self.startLevel = "room 1"
        self.visibleSprites.lights = False
        self.lightsOff = False
        for sprite in self.worldSprites:
            sprite.kill()
        
        self.createLevel(self.level)
        
    def interact(self):
        for sprite in self.interactiveSprites:
            if sprite.rect.colliderect(self.player.rect) and self.level != "room 7":
                sprite.activate()                        

    def changeRoom(self):
        for sprite in self.doorSprites:
            if sprite.rect.colliderect(self.player.rect):     
                if sprite.status == "closed":
                    coords = doorDests[self.level][sprite.rect.topleft]["coords"]
                    self.player.hitbox.topleft = coords
                    level = doorDests[self.level][sprite.rect.topleft]["room"]
                    self.player.combo = []
                    self.level = level
                    for sprite in self.worldSprites: sprite.kill()
                    self.createLevel(self.level)
                elif sprite.status == "trapped" and self.player.canTakeDamage:
                    self.player.health -= 50
                    self.player.canTakeDamage = False
                    self.player.damageTime = pygame.time.get_ticks()
                    self.player.direction.y = 15
    
    def checkDoor(self):
        if self.player.combo == ['omega', 'phi', 'psi', 'xi', 'pi']:
            for sprite in self.exit:
                sprite.changeState()
        else:
            if len(self.player.combo) == 5:
                self.player.combo = []
                for sprite in self.buttons:
                    sprite.reset()
        
    def usePortal(self):
        for sprite in self.portal:
            if sprite.rect.colliderect(self.player.rect) and pygame.key.get_pressed()[pygame.K_e]:
                if sprite.on:
                    return True
            
    def useItem(self,index):
            item = self.player.inventory[index]
            if item == "../graphics/sprites/idol.png":
                self.player.inventory[index] = None
                self.startLevel = self.level
                self.player.idolUsed = True
                self.player.idolPos = self.level
                self.playerPos = self.player.rect.topleft
            elif item == "../graphics/sprites/corrupted time.png":
                self.player.inventory[index] = None
                self.offsetTime = 10
                self.sleepPercent += 25
            elif item == "../graphics/sprites/key.png":
                for sprite in self.doorSprites:
                    if sprite.status == "locked" and sprite.rect.colliderect(self.player.rect):
                        self.player.inventory[index] = None
                        sprite.changeState()
            elif item == "../graphics/sprites/gem.png":
                for sprite in self.alter:
                    if sprite.rect.colliderect(self.player.rect):
                        self.player.inventory[index] = None
                        sprite.active()
                        for sprite in self.portal:
                            sprite.on = True
                            sprite.activate()

    def trapPit(self):
        for pitSprite in self.pitSprites:
            if pitSprite.rect.colliderect(self.player.hitbox2):
                for safeSprite in self.safeSprites:
                    if safeSprite.rect.colliderect(self.player.hitbox2):
                        return False
                return True

    def fireBalls(self,pos,direction):
        Ball(pos,[self.visibleSprites,self.harmSprites,self.worldSprites],direction)

    def update(self):
        if self.lightsOff:
            self.turnOffTheLights()
            if self.level == "room 7":
                for sprite in self.interactiveSprites: 
                    if sprite.rect.topleft != (64,64):
                        sprite.activate()
                        Door((320, 192),[self.visibleSprites,self.doorSprites,self.worldSprites],"../graphics/sprites/doors/doorup.png","up","closed")
        self.visibleSprites.custom_draw(self.player,self.level)
        self.trapSprites.update(self.player,self.collisionSprites)
        self.timer()
        self.showBar(10,self.player.health,self.player.stats["health"],"#ff0000")
        self.shooterSprites.update(self.fireBalls)
        self.harmSprites.update(self.player,self.collisionSprites)
        if self.trapPit():
            self.player.health = 0
        self.checkDoor()
        self.player.update(self.level,self.safeSprites)
        
        

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.lights = False

    def custom_draw(self,player,level):
        self.floor_surf = pygame.image.load(f'../graphics/map/levels/{level}/csv/{level}.png').convert_alpha()
        
        if level == "room 6" and self.lights:
            self.floor_surf = pygame.image.load(f'../graphics/map/levels/{level}/csv/{level}off.png').convert_alpha()
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
        
        hotbarImg = pygame.image.load("../graphics/sprites/hotbar.png").convert_alpha()
        hotbarImg = pygame.transform.scale_by(hotbarImg,1.5)
        hotbarRect = hotbarImg.get_rect(center = (SCREENWIDTH//2,740))       
        self.display_surface.blit(hotbarImg,hotbarRect)
        
        for index,image in enumerate(player.inventory):
            if image:
                image = pygame.image.load(image).convert_alpha()
                image = pygame.transform.scale_by(image,4)
                rect = image.get_rect(center = (438+index*109,740))
                self.display_surface.blit(image,rect)
    
    def turnOffTheLights(self):
        self.lights = True
