from entity import Entity
from pygame import Rect, image, transform, draw


class Tour_archer(Entity):
    def __init__(self, x:int,y:int,width:int,height:int,id:int,jd:int):
        self.image_path = "images\\"+"\\Towers\\Archer\\archer_level_1.png"
        super().__init__(x, y, width, height ,id,jd, self.image_path)
        self.hp = 100
        self.shoot_timer0 = 50
        self.shoot_timer = 0
    
    def change_img_lvl(self,lvl):
        self.image_path = "images\\"+"\\Towers\\Archer\\archer_level_"+str(self.level)+".png"
        self.load_image(self.image_path)
    
    @staticmethod
    def draw_item(display,x:int,y:int,width:int,height:int,selected=False):
        image_path = "images\\"+"\\Towers\\Archer\\archer_level_1.png"
        Image = transform.scale(image.load(image_path),(width,height))
        display.blit(Image,Rect(x,y,width,height))
        if(selected):
            draw.rect(display,(250,200,200),Rect(x,y,width,height),1)
    
    def loop(self,map):
        pass
