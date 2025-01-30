from pygame import KEYDOWN, MOUSEBUTTONUP, draw, Rect

class Map:
    def __init__(self,x:int,y:int,width:int,height:int,nx:int,ny:int):
        self.nx = nx
        self.ny = ny
        self.move(x,y,width,height)
        self.color = (60,150,90)
        self.color_line = (50,140,80)
        self.create_liste()
        self.next_place = None
    
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
            if(self.next_place is not None):
                self.place_id(self.next_place,id,jd)
                self.next_place = None
            
        elif (event.type == KEYDOWN):
            print(f"event : map[{id},{jd}] ->",event)
            
            dx=0
            dy=0
            print(event.key)
            if(event.key==1073741903):
                self.moves(1,0)
            elif(event.key==1073741904):
                self.moves(-1,0)
            if(event.key==1073741905):
                self.moves(0,1)
            elif(event.key==1073741906):
                self.moves(0,-1)
        
        if(not self.liste[id][jd] is None):
            self.liste[id][jd].events(event,mouse_pos,self)

    
    
    def place_new(self,item:object,x,y):
        id = int((x-self.x)//self.dx)
        jd = int((y-self.y)//self.dy)
        
        self.liste[id][jd] = item(x=self.x+id*self.dx,y=self.y+jd*self.dy,width=self.dx,height=self.dy,image=None)
    
    def place_id(self,item,i,j):
        self.liste[i][j] = item(x=self.x+i*self.dx,y=self.y+j*self.dy,width=self.dx,height=self.dy,image=None)
    
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
        string = ""
        for i in range(len(self.liste)):
            string += self.liste[i].__str__()+"\n"
        return string
    def __repr__(self):
        return self.___str___()
    

    def __getitem__(self,key):
        return self.liste[key]
    
    def moves(self, dx, dy):
        if dx > 0:
            range_i = range(len(self.liste) - 1, -1, -1)
            range_j = range(len(self.liste[0]) - 1, -1, -1)
        elif dx < 0:
            range_i = range(len(self.liste))
            range_j = range(len(self.liste[0]))
        elif dy > 0:
            range_i = range(len(self.liste) - 1, -1, -1)
            range_j = range(len(self.liste[0]) - 1, -1, -1)
        else:
            range_i = range(len(self.liste))
            range_j = range(len(self.liste[0]))

        for i in range_i:
            for j in range_j:
                if self.liste[i][j] is not None and self.liste[i][j].selected:
                    if 0 <= i + dx < len(self.liste) and 0 <= j + dy < len(self.liste[i]) and self.liste[i + dx][j + dy] is None:
                        item = self.liste[i][j]
                        self.liste[i + dx][j + dy] = item
                        self.liste[i][j] = None
                        item.move(self.x + (i + dx) * self.dx, self.y + (j + dy) * self.dy)

        
    def want_to_place(self, item):
        if self.next_place is None:
            self.next_place = item
            return True
        return False