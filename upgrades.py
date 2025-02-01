from pygame import MOUSEBUTTONUP, Rect, draw

from button import Button

class Upgrade:
    def __init__(self,x:int,y:int,width:int,height:int):
        self.move(x,y,width,height)
        self.color = (255, 204, 0)
        self.items = [Button(),Button(),Button()]
        self.selected = None
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
        for i in range(len(self.items)):
            item = self.items[i]
            item.draw(display,
                            x = self.x + self.width*0.1,
                            y = self.y + i*self.height*0.2 + (i+1)*self.height*0.1,
                            width = self.width*0.8,
                            height = self.height*0.2,
                            selected = self.selected == i)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEBUTTONUP):
            print("event : upgrade menu ->",event)
    
        for i in range(len(self.items)):
            x = self.x + self.width*0.1
            y = self.y + i*self.height*0.2 + (i+1)*self.height*0.1
            width = self.width*0.8
            height = self.height*0.2
        
            rect = Rect(x,y,width,height)
            if(rect.collidepoint(mouse_pos)):
                self.items[i].events(event,mouse_pos)
                self.selected = i
                
                if(event.type == MOUSEBUTTONUP):
                    print(f"event : upgrade menu[{i}] ->",event)
        