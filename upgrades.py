from pygame import MOUSEBUTTONUP, Rect, draw

from button import Button

class Upgrade:
    def __init__(self,x:int,y:int,width:int,height:int):
        self.move(x,y,width,height)
        self.color = (255, 204, 0)
        self.items = [Button(text="delete"),Button(text="move"),Button(text="upgrade"),Button(text="rotate")]
        self.selected = None
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def get_button_pos(self,i:int):
        '''
        return -> (x,y,width,height)
        '''
        x = self.x + 5
        y = self.y + i*self.height*0.15 + (i+1)*self.height*0.06
        width = self.width-10
        height = self.height*0.2
        return (x,y,width,height)
    
    def draw(self,display,activated:bool):
        draw.rect(display,self.color,self.rect)
        if(activated):
            for i in range(len(self.items)):
                item = self.items[i]
                button_pos = self.get_button_pos(i)
                item.draw(display,
                                button_pos[0],
                                button_pos[1],
                                button_pos[2],
                                button_pos[3],
                                selected = self.selected == i)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEBUTTONUP):
            print("event : upgrade menu ->",event)
    
        for i in range(len(self.items)):
            button_pos = self.get_button_pos(i)
        
            rect = Rect(button_pos[0],button_pos[1],button_pos[2],button_pos[3])
            if(rect.collidepoint(mouse_pos)):
                self.items[i].events(event,mouse_pos,map=map)
                self.selected = i
                
                if(event.type == MOUSEBUTTONUP):
                    print(f"event : upgrade menu[{i}] ->",event)
        