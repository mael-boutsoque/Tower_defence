from pygame import KEYDOWN, MOUSEBUTTONUP, draw, Rect

class Map:
    def __init__(self,x:int,y:int,width:int,height:int,nx:int,ny:int):
        self.nx = nx
        self.ny = ny
        self.move(x,y,width,height)
        self.color = (60,150,90)
        self.color_line = (50,140,80)
        self.create_liste()
    
    def move(self,x=0,y=0,width=0,height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(self.x,self.y,self.width,self.height)
        self.dx = self.width/self.nx
        self.dy = self.height/self.ny
    
    def create_liste(self):
        self.liste = []
        for i in range(self.ny):
            self.liste.append([None]*self.nx)
        print(self.liste)
        
    
    def draw(self,display):
        draw.rect(display,self.color,self.rect)
        for i in range(self.nx):
            for j in range(self.ny):
                draw.rect(display,self.color_line,Rect(i*self.dx,j*self.dy,self.dx,self.dy),width=2)
                
                if (not self.liste[i][j] is None):
                    self.liste[i][j].draw(display)
                
    
    def events(self,event,mouse_pos):
        id = int((mouse_pos[0]-self.x)//self.dx)
        jd = int((mouse_pos[1]-self.y)//self.dy)
        if (event.type == MOUSEBUTTONUP):
            print(f"event : map[{id},{jd}] ->",event)
        elif (event.type == KEYDOWN):
            print(f"event : map[{id},{jd}] ->",event)
        
        if(not self.liste[id][jd] is None):
            self.liste[id][jd].events(event,mouse_pos)
    
    
    def place(self,item:object,x,y):
        id = int((x-self.x)//self.dx)
        jd = int((y-self.y)//self.dy)
        
        self.liste[id][jd] = item(x=self.x+id*self.dx,y=self.y+jd*self.dy,width=self.dx,height=self.dy,image=None)
        print(self)
    
    def place_id(self,item,i,j):
        self.liste[i][j] = item(x=self.x+i*self.dx,y=self.y+j*self.dy,width=self.dx,height=self.dy,image=None)
        print(self)
    
    def place_on_free(self,item):
        looping= True
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if(self.liste[i][j] is None):
                    self.place_id(item,i,j)
                    looping = False
                    break
            if(not looping):
                break
    
    def ___str___(self):
        return self.liste.__str__()
    def __repr__(self):
        return self.___str___()
    

    def __getitem__(self,key):
        return self.liste[key]