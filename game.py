import pygame
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
        self.menu = Menu(self.width*(1-0.2),0,self.width*0.2,self.height,[])
        self.entitee = Entity(500,500,100,100)
        self.loop()
    
    
    def loop(self):
        while self.running:
            self.events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
    
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw(self):
        self.display.fill((0,0,0))
        self.menu.draw(self.display)
        self.entitee.draw(self.display)