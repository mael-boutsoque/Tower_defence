from entity import Entity
from token_1 import Token

class Generator(Entity):
    image = "generator"
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        super().__init__(x,y,width,height,id,jd)
        self.delay0 = 200
        self.delay = self.delay0
    
    def loop(self,map):
        if(self.delay>0):
            self.delay -= 1
        else:
            self.delay = self.delay0
            self.token = Token(1,self.x,self.y,self.ids[0],self.ids[1])
            self.spit_token(map)
