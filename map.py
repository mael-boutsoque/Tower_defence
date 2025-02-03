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
        self.next_old_id = (None,None)
        self.selected = None
        self.selected_id = (None,None)
    
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
                
    
    def events(self,event,mouse_pos,menu):
        id = int((mouse_pos[0]-self.x)//self.dx)
        jd = int((mouse_pos[1]-self.y)//self.dy)
        if (event.type == MOUSEBUTTONUP):
            print(f"event : map[{id},{jd}] select{self.selected_id} to_place[{self.next_place}] ->",event)
            if(self.next_place is not None):
                self.place_id(self.next_place,id,jd)
                self.next_place = None
                menu.selected = None
            
            elif(id<self.nx and jd<self.ny and not self.liste[id][jd] is None):
                self.deselect_all()
                self.liste[id][jd].events(event,mouse_pos,self)
                self.selected = self.liste[id][jd]
                self.selected_id = (id,jd)
            
        elif (event.type == KEYDOWN):
            print(f"event : map[{id},{jd}] ->",event)
            if(event.type == KEYDOWN):
                if(event.key==27):
                    menu.selected = None
                    if(not self.next_place is None):
                        if(self.next_old_id != (None,None)):
                            self.place_id(self.next_place,self.next_old_id[0],self.next_old_id[1])
                            self.next_old_id = (None,None)
                        self.next_place = None
                    else:
                        self.deselect_all()
    
            print(event.key)
            if(event.key==1073741903):
                self.moves(1,0)
            elif(event.key==1073741904):
                self.moves(-1,0)
            if(event.key==1073741905):
                self.moves(0,1)
            elif(event.key==1073741906):
                self.moves(0,-1)

    
    
    def place_new(self,item:object,x,y):
        id = int((x-self.x)//self.dx)
        jd = int((y-self.y)//self.dy)
        
        self.liste[id][jd] = item(x=self.x+id*self.dx,y=self.y+jd*self.dy,width=self.dx,height=self.dy,image=None)
    
    def place_id(self,item,i,j):
        item_is_new = type(item) is type
        if(i<self.nx and j<self.ny and self.liste[i][j] is None):
            if(item_is_new):
                item = item(x=self.x+i*self.dx,y=self.y+j*self.dy,width=self.dx,height=self.dy,image=None)
                self.liste[i][j] = item
            else:
                self.liste[i][j] = item
                self.liste[i][j].move(self.x+i*self.dx,self.y+j*self.dy)
        elif(self.next_old_id != (None,None) and not item_is_new):
            self.place_id(item,self.next_old_id[0],self.next_old_id[1])

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
    
    def deselect_all(self):
        self.selected = None
        self.selected_id = (None,None)
        for i in range(len(self.liste)):
            for j in range(len(self.liste[i])):
                if self.liste[i][j] is not None:
                    self.liste[i][j].selected = False
    
    def delete_selected(self):
        if self.selected is not None:
            self.liste[self.selected_id[0]][self.selected_id[1]] = None
            self.selected = None
            self.selected_id = (None,None)
    
    def get_selected_pos(self):
        return self.selected_id
    
    def upgrade_selected(self):
        if self.selected is not None:
            self.selected.upgrade()