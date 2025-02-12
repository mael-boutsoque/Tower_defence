from pygame import MOUSEBUTTONUP, Rect, image, transform, draw
from numpy import cos, sin, pi

class Entity:
    color = {0:(0, 153, 0),1:(0, 204, 102),2:(0, 153, 153),3:(0, 102, 204),4:(0, 0, 255),5:(102, 0, 255),6:(204, 0, 255),7:(204, 0, 153),8:(204, 0, 102),9:(255, 0, 0),10:(255, 153, 0)}
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        self.image_path = self.get_image_path()
        self.move(id,jd,x,y,width,height)
        self.load_image(self.image_path)
        self.selected = False
        self.level = 1
        self.ids = (id,jd)
        self.token = None
        self.pick_delay0 = 50
        self.pick_delay = self.pick_delay0
        self.spit_delay0 = 50
        self.spit_delay = self.spit_delay0
        self.rotation = [1,0]
        self.angle = 0
        self.bg_color = Entity.color[0]
    
    @classmethod
    def get_image_path(cls,lvl=0)->str:
        if(lvl==0):
            return "images\\"+cls.__name__+".png"
        else:
            return "images\\"+cls.__name__+str(lvl)+".png"
    
    def move(self,id,jd,x=0,y=0,width=None,height=None):
        self.ids = (id,jd)
        self.x = x
        self.y = y
        self.width = width or self.width
        self.height = height or self.height
        self.rect = Rect(self.x+1,self.y+1,self.width-2,self.height-2)
    
    def load_image(self,image_path):
        print("load image",image_path)
        try:
            self.image = transform.scale(image.load(image_path),(self.width,self.height))
        except:
            self.image = transform.scale(image.load(Entity.get_image_path()),(self.width,self.height))
    
    def draw(self,display):
        draw.rect(display,self.bg_color,self.rect)
        display.blit(self.image,self.rect)
        if(self.selected):
            draw.rect(display,(250,200,200),self.rect,1)
        if(self.token is not None):
            draw.rect(display,(0,200,0),self.rect,2)
        self.draw_token(display)
        self.draw_rotation(display)
    
    def draw_token(self,display):
        if(self.token is not None):
            self.token.draw(display)
    
    @classmethod
    def draw_item(cls,display,x:int,y:int,width:int,height:int,selected=False):
        image_path = cls.get_image_path()
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
        if(self.level<10):
            print("upgrade",self)
            self.level += 1
            self.bg_color = Entity.color[self.level]
            self.upgrade_func()
    
    def upgrade_func(self):
        pass
    
    def ___str___(self):
        return f"Entity(x{self.x},y{self.y},i{self.ids[0]},j{self.ids[1]}|{self.token})"
    def __repr__(self):
        return self.___str___()
    
    def loop(self,map):
        pass
    
    # %% ROTATION
    def draw_rotation(self,display):
        draw.circle(display,(255,255,255),(self.x+(self.width/2)*(1+0.95*self.rotation[0]),self.y+(self.height/2)*(1+0.95*self.rotation[1])),2)
    
    def rotate(self,direction):
        self.angle += direction
        self.rotation = [int(cos(self.angle*pi/2)),int(sin(self.angle*pi/2))]
        print("RATATE",direction)
    
    # %% PICK AND SPIT TOKEN
    def pick_test(self,map):
        if(self.pick_delay>0):
            self.pick_delay -= 1
        else:
            self.pick_delay = self.pick_delay0
            self.pick_token(map)
    
    def spit_test(self,map):
        if(self.spit_delay>0):
            self.spit_delay -= 1
        else:
            self.spit_delay = self.spit_delay0
            self.spit_token(map)
    
    def spit_token(self,map):
        if(self.token is not None):
            map.move_token(self.token,self.ids[0]+self.rotation[0],self.ids[1]+self.rotation[1])
            self.token = None
    
    def pick_token(self,map):
        if(self.token is None):
            token = map.take_token(self.ids[0],self.ids[1])
            if(token is not None):
                self.token = token
            else:
                self.pick_delay = 0