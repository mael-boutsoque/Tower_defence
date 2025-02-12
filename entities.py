from entity import Entity
from token_1 import Token

class Generator(Entity):
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        super().__init__(x,y,width,height,id,jd)
        self.delay0 = 200
        self.delay = self.delay0
    
    def upgrade_func(self):
        self.delay0 -= 12
    
    def loop(self,map):
        if(self.delay>0):
            self.delay -= 1
        else:
            self.delay = self.delay0
            self.token = Token(1,self.x,self.y,self.ids[0],self.ids[1])
            self.spit_token(map)


class Seller(Entity):
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        super().__init__(x,y,width,height,id,jd)
        self.pick_delay0 = 20
        self.spit_delay0 = 50
    
    def upgrade_func(self):
        self.pick_delay0 = max(self.pick_delay0-2,1)
        self.spit_delay0 = max(self.spit_delay0-2,1)
    
    def sell_token(self):
        if(self.token is not None):
            value = self.token.get_value()
            print(f"sell token {value}$ !!!NOT IMPLEMENTED!!!")
            self.token = None
    
    def loop(self,map):
        if(self.spit_delay>0):
            self.spit_delay -= 1
        else:
            self.spit_delay = self.spit_delay0
            self.sell_token()
        
        self.pick_test(map)


class Adder(Entity):
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        super().__init__(x,y,width,height,id,jd)
        self.pick_delay0 = 20
        self.add_value = 2
    
    def upgrade_func(self):
        self.add_value += 3
    
    def spit_token(self, map):
        if(self.token is not None):
            self.token.value += self.add_value
        super().spit_token(map)
    
    def loop(self,map):
        self.pick_test(map)
        self.spit_test(map)

class Multiplier(Entity):
    def __init__(self,x:int,y:int,width:int,height:int,id:int,jd:int):
        super().__init__(x,y,width,height,id,jd)
        self.pick_delay0 = 20
        self.mult_value = 2
    
    def upgrade_func(self):
        self.mult_value += 1
    
    def spit_token(self, map):
        if(self.token is not None):
            self.token.value = self.token.value*self.mult_value
        super().spit_token(map)
    
    def loop(self,map):
        self.pick_test(map)
        self.spit_test(map)