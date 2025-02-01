from pygame import MOUSEBUTTONUP, Rect, transform, image, draw


class Button:
    image = "no_texture.png"
    def __init__(self,image=None,text:str=""):
        if(image is None):
            self.image_path = "images\\"+Button.image
        self.load_image(self.image_path)
    
    def load_image(self,image_path):
        self.image = image.load(image_path)
    
    def resize_image(self,width:int,height:int):
        self.image = transform.scale(self.image,(width,height))
    
    def draw(self,display,x:int,y:int,width:int,height:int,selected=False):
        self.resize_image(width,height)
        rect = Rect(x,y,width,height)
        display.blit(self.image,rect)
        if(selected):
            draw.rect(display,(250,200,200),rect,1)
    
    def events(self,event,mouse_pos):
        if(event.type == MOUSEBUTTONUP):
            print("event : button ->",event)