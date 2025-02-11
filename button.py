from pygame import MOUSEBUTTONUP, Rect, transform, image, draw, font


class Button:
    image = "Entity.png"
    def __init__(self,image=None,text:str=""):
        if(image is None):
            self.image_path = "images\\"+Button.image
        self.load_image(self.image_path)
        self.text = text
        self.color_bg = (201, 50, 50)
        self.color_text = (0, 0, 0)
        self.font = font.SysFont('Comic Sans MS', 20)
    
    def load_image(self,image_path):
        self.image = image.load(image_path)
    
    def resize_image(self,width:int,height:int):
        self.image = transform.scale(self.image,(width,height))
    
    def draw(self,display,x:int,y:int,width:int,height:int,selected=False):
        rect = Rect(x,y,width,height)
        img_coef = min(width,height)
        img_size = 0.8*img_coef
        rect_img = Rect(x+0.1*img_coef,
                        y+0.1*img_coef,
                        img_size,
                        img_size)
        self.resize_image(img_size,img_size)
        draw.rect(display,self.color_bg,rect)
        display.blit(self.image,rect_img)
        text_surface = self.font.render(self.text, False, self.color_text)
        display.blit(text_surface,(x+img_coef,y+img_coef*0.1))
        if(selected):
            draw.rect(display,(250,200,200),rect,1)
    
    def events(self,event,mouse_pos,map):
        if(event.type == MOUSEBUTTONUP):
            print("event : button ->",event)
            if(self.text == "delete"):
                self.delete(map)
            if(self.text == "move"):
                self.move(map)
            if(self.text == "upgrade"):
                self.upgrade(map)
    
    
    def delete(self,map):
        print("delete")
        map.delete_selected()
    
    def move(self,map):
        print("move")
        if(map.next_place is None):
            pos = map.get_selected_pos()
            map.deselect_all()
            map.next_place = map.liste[pos[0]][pos[1]]
            map.next_old_id = pos
            map.liste[pos[0]][pos[1]] = None
    
    def upgrade(self,map):
        print("upgrade")
        map.upgrade_selected()
        