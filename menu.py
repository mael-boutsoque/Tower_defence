from pygame import draw, Rect


class Menu:
    def __init__(self,x:int,y:int,width:int,height:int,items:list):
        self.items = items
        self.move(x,y,width,height)
        self.color = (60,150,90)
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)