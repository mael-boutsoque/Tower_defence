from pygame import Rect, draw


class Token:
    def __init__(self, value:int, x:int, y:int, radius:int, id, jd,color=None):
        self.value = value
        self.radius = radius
        self.id = id
        self.jd = jd
        self.move(id,jd,x,y)
        if(color is None):
            self.color = (255,0,0)
    
    def move(self,id,jd,x,y):
        self.id = id
        self.jd = jd
        self.x = x
        self.y = y
        self.rect = Rect(self.x,self.y,self.radius,self.radius)

    def draw(self,display):
        draw.circle(display,self.color,(self.x+self.radius/2,self.y+self.radius/2),self.radius)
        draw.circle(display,(255,255,255),(self.x+self.radius/2,self.y+self.radius/2),self.radius,width=1)
    
    def ___str___(self):
        return f"Token(x{self.x},y{self.y}|i{self.id},j{self.jd}|{self.value})"
    def __repr__(self):
        return self.___str___()

