import pygame

class Game():
    def __init__(self, width, height):
        pygame.init()
        self.display = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
    
    def run(self):
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
        pygame.draw.rect(self.display,(255,255,255),pygame.Rect(100,100,100,100))