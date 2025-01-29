from pygame import Rect, image, transform

class Entity:
    def __init__(self,x:int,y:int,width:int,height:int,image="no_texture.png"):
        self.image_path = "images\\"+image
        self.move(x,y,width,height)
        self.load_image(self.image_path)
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def load_image(self,image_path):
        self.image = transform.scale(image.load(image_path),(self.width,self.height))
    
    def draw(self,display):
        display.blit(self.image,self.rect)