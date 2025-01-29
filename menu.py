from pygame import draw, Rect


class Menu:
    def __init__(self,x:int,y:int,width:int,height:int,items:list):
        self.items = items
        self.move(x,y,width,height)
        self.color = (60,150,90)
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
        for i in range(len(self.items)):
            item = self.items[i]
            item.draw_item(display,
                            x = self.x + self.width*0.1,
                            y = self.y + self.height*0.1 + i*(self.width*0.8+self.width*0.1) ,
                            width = self.width*0.8,
                            height = self.width*0.8)
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)