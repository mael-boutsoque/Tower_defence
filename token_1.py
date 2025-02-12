from pygame import Rect, draw, font


class Token:
    def __init__(self, value:int, x:int, y:int, id, jd, radius = 14,color=None):
        self.value = value
        self.radius = radius
        self.id = id
        self.jd = jd
        self.move(id,jd,x,y)
        if(color is None):
            self.color = (255,0,0)
        self.font = font.SysFont('Trebuchet ', 20)
    
    def move(self,id,jd,x,y):
        self.id = id
        self.jd = jd
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,self.radius,self.radius)

    def draw(self,display):
        font_size = self.font.size(str(self.value))[0]
        size = max(font_size,self.radius)
        draw.circle(display,self.color,(self.x+size/2,self.y+size/2-font_size/2),size)
        text = self.font.render(str(self.value),False,(255,255,255))
        display.blit(text,(self.x,self.y))
        draw.circle(display,(255,255,255),(self.x+size/2,self.y+size/2-font_size/2),size,width=1)
    
    def get_value(self)->int:
        return self.value
    
    def ___str___(self):
        return f"Token(x{self.x},y{self.y}|i{self.id},j{self.jd}|{self.value})"
    def __repr__(self):
        return self.___str___()
