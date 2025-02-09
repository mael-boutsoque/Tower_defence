from pygame import Rect, transform, image, draw

class Monster:
    image = "no_texture"
    def __init__(self,x:int,y:int,width:int,height:int,ligne):
        self.move(x,y,width,height)
        self.load_image("images\\"+Monster.image+".png")
        self.dead = False
        self.hp = 100
        self.speed = 10
        self.ligne = ligne

    def draw(self,display):
        display.blit(self.image,self.rect)
    
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
            self.image = transform.scale(image.load("images\\"+Monster.image+".png"),(self.width,self.height))
    
    def events(self,event,mouse_pos,map):
        pass
    
    def ___str___(self):
        return f"Monster[pos = ({round(self.x)},{round(self.y)}) | size = ({self.width},{self.height})]"
    def __repr__(self):
        return self.___str___()
    
    def loop(self,map):
        if(self.can_move(map)):
            self.move(self.x-0.01*self.speed,self.y)
    
    def can_move(self,map):
        if(self.x<0):
            self.dead = True
            return False
        if(map.get_by_pos(self.x,self.y) is None):
            return True