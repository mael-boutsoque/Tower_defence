from pygame import KEYDOWN, draw, Rect, MOUSEWHEEL, MOUSEBUTTONUP


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
            #check if item is in the menu display
            x = self.x + self.width*0.1
            y = self.y + i*self.width*0.8 + (i+1)*self.width*0.1 + self.scroll
            if(y < self.y + self.height):
                item.draw_item(display,
                                x =x,
                                y = y,
                                width = self.width*0.8,
                                height = self.width*0.8,
                                selected = i==self.selected)
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def events(self,event,mouse_pos,map):
        if(map.next_place is None):
            self.selected = None
        if(event.type == KEYDOWN):
            if(event.key==27):
                self.selected = None
                if(map.next_old_id != (None,None)):
                    map.next_place = None
        if(event.type == MOUSEWHEEL):
            print("event : menu scroll ->",event.y)
            if((self.scroll + event.y * self.height // 5 <= 0 and event.y>0) or (self.scroll + event.y * self.height // 5 > self.height - (len(self.items)+1)*(self.width*0.9) and event.y<0)):
                self.scroll += event.y * self.height // 4
        
        elif(event.type == MOUSEBUTTONUP and (event.button!=4 and event.button!=5)):
            for i in range(len(self.items)):
                x = self.x + self.width*0.1
                y = self.y + i*self.width*0.8 + (i+1)*self.width*0.1 + self.scroll
                width = self.width*0.8
                height = self.width*0.8
                
                rect = Rect(x,y,width,height)
                if(rect.collidepoint(mouse_pos) and map.next_place is None):
                    self.items[i].events_static(event,mouse_pos)
                    map.want_to_place(self.items[i])
                    self.selected = i        