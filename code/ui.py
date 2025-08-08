import pygame
from settings import *
import sys

class MainMenu:
    def __init__(self,screen):
        self.screen = screen

        #logo
        self.logo = pygame.image.load("../graphics/logo/LoopZ.png").convert_alpha()
        self.logo = pygame.transform.scale_by(self.logo,2)
        self.logoRect = self.logo.get_rect(center = (SCREENWIDTH//2,SCREENHEIGHT//4.5))

        #button setup
        self.quitButton = pygame.image.load("../graphics/buttons/exit.png")
        self.quitButton = pygame.transform.scale_by(self.quitButton,2)
        self.quitRect = self.quitButton.get_rect(center = (SCREENWIDTH//2,SCREENHEIGHT//1.3))

        self.playButton = pygame.image.load("../graphics/buttons/play.png")
        self.playButton = pygame.transform.scale_by(self.playButton,2)
        self.playRect = self.playButton.get_rect(center = (SCREENWIDTH//2,SCREENHEIGHT//2))

    def draw(self):
        self.screen.fill("#1D181F")
        self.screen.blit(self.logo,self.logoRect)
        self.screen.blit(self.quitButton,self.quitRect)
        self.screen.blit(self.playButton,self.playRect)

    def checkPushed(self,button):
        self.mouse = pygame.mouse.get_pressed()
        self.mousePos = pygame.mouse.get_pos()
        

        if button.collidepoint(self.mousePos[0],self.mousePos[1]) and self.mouse[0]:
            return True

    def update(self):
        self.draw()
        if self.checkPushed(self.quitRect):
            pygame.quit()
            sys.exit()

class WinScreen:
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load("../graphics/logo/win.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,0))

        #button setup
        self.quitButton = pygame.image.load("../graphics/logo/quit.png").convert_alpha()
        self.quitRect = self.quitButton.get_rect(center = (SCREENWIDTH//2,SCREENHEIGHT//1.3))

    def draw(self):
        self.screen.fill("#1D181F")
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.quitButton,self.quitRect)


    def checkPushed(self,):
        self.mouse = pygame.mouse.get_pressed()
        self.mousePos = pygame.mouse.get_pos()
        

        if self.quitRect.collidepoint(self.mousePos[0],self.mousePos[1]) and self.mouse[0]:
            return True

    def update(self):
        self.draw()