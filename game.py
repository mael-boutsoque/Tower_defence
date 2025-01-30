import pygame
from map import Map
from menu import Menu
from entity import Entity

class Game():
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
    
    def run(self):
        menuwidth = min(140,self.width*0.2)
        self.menu = Menu(self.width-menuwidth,0,menuwidth,self.height,[Entity,Entity,Entity,Entity])
        self.map = Map(0,0,self.width-menuwidth,self.height,10,10)
        self.map.place_new(Entity,100,100)
        self.loop()
    
    
    def loop(self):
        while self.running:
            self.events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
    
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==27):
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                print(event.key)
            
            mouse_pos = pygame.mouse.get_pos()
            if(self.menu.rect.collidepoint(mouse_pos)):
                self.menu.events(event,mouse_pos,self.map)
            elif(self.map.rect.collidepoint(mouse_pos)):
                self.map.events(event,mouse_pos)
    
    def draw(self):
        self.display.fill((0,0,0))
        self.menu.draw(self.display)
        self.map.draw(self.display)