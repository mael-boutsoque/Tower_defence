from pygame import draw, Rect, MOUSEWHEEL, MOUSEBUTTONUP

from entity import Entity


class Menu:
    def __init__(self,x:int,y:int,width:int,height:int,items:list):
        self.items = items
        self.move(x,y,width,height)
        self.color = (90,70,150)
        self.scroll = 0
        self.selected = None
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
        for i in range(len(self.items)):
            item = self.items[i]
            item.draw_item(display,
                            x = self.x + self.width*0.1,
                            y = self.y + i*self.width*0.8 + (i+1)*self.width*0.1 + self.scroll,
                            width = self.width*0.8,
                            height = self.width*0.8)
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEWHEEL):
            print("event : menu scroll ->",event.y)
            self.scroll += event.y * 10
        
        elif(event.type == MOUSEBUTTONUP and (event.button!=4 and event.button!=5)):
            for i in range(len(self.items)):
                x = self.x + self.width*0.1
                y = self.y + i*self.width*0.8 + (i+1)*self.width*0.1 + self.scroll
                width = self.width*0.8
                height = self.width*0.8
                
                rect = Rect(x,y,width,height)
                if(rect.collidepoint(mouse_pos)):
                    self.items[i].events_static(event,mouse_pos)
                    map.want_to_place(self.items[i])
                    print(map)
        