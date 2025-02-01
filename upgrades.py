from pygame import MOUSEBUTTONUP, Rect, draw

class Upgrade:
    def __init__(self,x:int,y:int,width:int,height:int):
        self.move(x,y,width,height)
        self.color = (255, 204, 0)
        self.scroll = 0
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEBUTTONUP):
            print("event : upgrade menu ->",event)
    