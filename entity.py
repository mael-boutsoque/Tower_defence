from pygame import MOUSEBUTTONUP, Rect, image, transform, draw

class Entity:
    image = "no_texture"
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int,image=None):
        if(image is None):
            self.image_path = "images\\"+Entity.image+".png"
        self.move(id,jd,x,y,width,height)
        self.load_image(self.image_path)
        self.selected = False
        self.level = 1
        self.ids = (id,jd)
        self.token = None
        self.delay0 = 50
        self.delay = self.delay0
        self.rotation = [1,0]
    
    def move(self,id,jd,x=0,y=0,width=None,height=None):
        self.ids = (id,jd)
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
        if(self.token is not None):
            draw.rect(display,(0,200,0),self.rect,2)
    
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
            self.change_img_lvl(self.level)
    
    def change_img_lvl(self,lvl):
        self.image_path = f"images\\{Entity.image}{self.level}"+".png"
        self.load_image(self.image_path)
    
    def ___str___(self):
        return f"Entity(x{self.x},y{self.y},i{self.ids[0]},j{self.ids[1]}|{self.token})"
    def __repr__(self):
        return self.___str___()
    
    def loop(self,map):
        if(self.delay>0):
            self.delay -= 1
        else:
            self.delay = self.delay0
            if(self.token is None):
                token = map.take_token(self.ids[0],self.ids[1])
                if(token is not None):
                    self.token = token
                    print("take token",self)
                else:
                    self.delay = 0
            else:
                map.move_token(self.token,self.ids[0]+self.rotation[0],self.ids[1]+self.rotation[1])
                self.token = None
        