import pygame
from map import Map
from menu import Menu
from entity import Entity
from upgrades import Upgrade
from entities import *

class Game():
    def __init__(self, width, height , nx , ny):
        '''
        # Start the game
        nx = number of box horizontally
        ny = number of box verticaly
        '''
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width,height),pygame.RESIZABLE)
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        self.nx = nx
        self.ny = ny
        pygame.font.init()
    
    def run(self):
        self.map = Map(0,0,self.width,self.height,self.nx,self.ny)
        menuwidth = max(140,self.width-self.map.width)
        self.menu = Menu(self.width-menuwidth,0,menuwidth,self.height*0.6,[Generator,Seller,Adder,Multiplier,Entity])
        self.upgrade = Upgrade(self.width-menuwidth,self.height*0.5,menuwidth,self.height*0.5)
        self.loop()
    
    def resize(self):
        self.map.move(0,0,self.width,self.height)
        menuwidth = max(140,self.width-self.map.width)
        self.menu.move(self.width-menuwidth,0,menuwidth,self.height*0.6)
        self.upgrade.move(self.width-menuwidth,self.height*0.5,menuwidth,self.height*0.5)
    
    
    def loop(self):
        while self.running:
            self.events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
    
    
    def events(self):
        self.map.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# or (event.type == pygame.KEYDOWN and event.key==27):
                self.running = False
            
            if event.type == pygame.VIDEORESIZE:
                self.width = event.w
                self.height = event.h
                self.resize()
            
            #debbug
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 109:
                    print(self.map)
            
            mouse_pos = pygame.mouse.get_pos()
            if(self.upgrade.rect.collidepoint(mouse_pos)):
                self.upgrade.events(event,mouse_pos,map=self.map)
            elif(self.menu.rect.collidepoint(mouse_pos)):
                self.menu.events(event,mouse_pos,map=self.map)
            elif(self.map.rect.collidepoint(mouse_pos)):
                self.map.events(event,mouse_pos,menu=self.menu)
    
    def draw(self):
        self.display.fill((0,0,0))
        self.map.draw(self.display)
        self.menu.draw(self.display)
        self.upgrade.draw(self.display,activated=self.map.selected is not None)