import pygame
import sys
from settings import *
from level import Level
from ui import *

class Game:
    '''runs the game state to display the GUI window so the game can play,
    general setup for the game'''
    def __init__(self):
        #creates the window and changes the name 
        self.screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        pygame.display.set_caption("Loops")
        #controls FPS and tracks time for timer calculations
        self.clock = pygame.time.Clock()

        self.buttonPressed = False

        self.paused = False
        self.activeStatus = 0
        self.changeState()
        
    def run(self):
        '''controls the game's running per game tick,
        performs all of the methods which need to be ran for the game to function'''
        while True:
            #main event loop which checks for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()#uninitialises pygame
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused

            pygame.display.update()
            #sets the Frame rate
            self.clock.tick(60)
            
            #updating the game based on state
            if self.activeStatus == 0:
                self.mainMenu.update()
                if self.mainMenu.checkPushed(self.mainMenu.playRect):
                    self.activeStatus = 1
                    self.changeState()
                if self.mainMenu.checkPushed(self.mainMenu.quitRect):
                    if not self.buttonPressed:
                        pygame.quit()
                        sys.exit()
                else:
                    self.buttonPressed = False
            elif self.activeStatus == 1:
                if not self.paused:
                    self.level.update()
                    if self.level.player.health <= 0:
                        self.activeStatus = 0
                        self.changeState()
                    if self.level.usePortal():
                        self.activeStatus = 2
                        self.changeState()
                else:
                    self.pauseMenu.update()
            elif self.activeStatus == 2:
                self.win.update()
                if self.win.checkPushed():
                    self.activeStatus = 0
                    self.buttonPressed = True
                    self.changeState()
            
    def changeState(self):
        if self.activeStatus == 0:
            self.mainMenu = MainMenu(self.screen)
        if self.activeStatus == 1:
            self.level = Level(self.screen)
            self.pauseMenu = PauseMenu(self.screen)
        if self.activeStatus == 2:
            self.win = WinScreen(self.screen)
 
if __name__ == "__main__":
    game = Game()
    game.run()