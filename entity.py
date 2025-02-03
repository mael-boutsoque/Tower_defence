from pygame import MOUSEBUTTONUP, Rect, image, transform, draw

class Entity:
    image = "no_texture"
    def __init__(self,x:int,y:int,width:int,height:int,image=None):
        if(image is None):
            self.image_path = "images\\"+Entity.image+".png"
        self.move(x,y,width,height)
        self.load_image(self.image_path)
        self.selected = False
        self.level = 0
    
    def move(self,x=0,y=0,width=None,height=None):
        self.x = x
        self.y = y
        self.width = width or self.width
        self.height = height or self.height
        self.rect = Rect(self.x,self.y,self.width,self.height)
    
    def load_image(self,image_path):
        print("load image",image_path)
        try:
            self.image = transform.scale(image.load(image_path),(self.width,self.height))
        except:
            self.image = transform.scale(image.load("images\\"+Entity.image+".png"),(self.width,self.height))
    
    def draw(self,display):
        display.blit(self.image,self.rect)
        if(self.selected):
            draw.rect(display,(250,200,200),self.rect,1)
    
    @staticmethod
    def draw_item(display,x:int,y:int,width:int,height:int,selected=False):
        image_path = "images\\"+Entity.image+".png"
        Image = transform.scale(image.load(image_path),(width,height))
        display.blit(Image,Rect(x,y,width,height))
        if(selected):
            draw.rect(display,(250,200,200),Rect(x,y,width,height),1)
    
    @staticmethod
    def events_static(event,mouse_pos):
        print("event : item entity ->",event)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEBUTTONUP):
            print("event : basic entity(selected="+str(not self.selected)+") ->",event)
            self.selected = not self.selected
    
    def upgrade(self):
        print("upgrade",self)
        if(self.level<3):
            self.level += 1
            self.image_path = f"images\\{Entity.image}{self.level}"+".png"
            self.load_image(self.image_path)
    
    def ___str___(self):
        return f"Entity[pos = ({self.x},{self.y}) | size = ({self.width},{self.height})]"
    def __repr__(self):
        return self.___str___()