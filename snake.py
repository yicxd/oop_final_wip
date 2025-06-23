from game_object import GameObject
import curses
import sys

class Snake(GameObject):
    def __init__(self, name):
        super().__init__(name)
        self.direction = curses.KEY_RIGHT
        self.coords = [[0, 0], [0, 1], [0, 2], [0, 3]]
        self.field = None
        
    def set_direction(self, ch):
        if ch == curses.KEY_LEFT and self.direction == curses.KEY_RIGHT:
            return
        if ch == curses.KEY_RIGHT and self.direction == curses.KEY_LEFT:
            return
        if ch == curses.KEY_UP and self.direction == curses.KEY_DOWN:
            return
        if ch == curses.KEY_DOWN and self.direction == curses.KEY_UP:
            return 
        self.direction = ch

    def move(self):
        head = self.coords[-1][:] #coords of the head
        head = self._check_limit(head) #checks limit of the field through head

        #new updating coords of the head
        if self.direction == curses.KEY_UP:
            head[0]-=1
        elif self.direction == curses.KEY_DOWN:
            head[0]+=1
        elif self.direction == curses.KEY_RIGHT:
            head[1]+=1
        elif self.direction == curses.KEY_LEFT:
            head[1]-=1

        del(self.coords[0])
        self.coords.append(head)
        self.field.snake_coords = self.coords

        if not self.snake_alive(): #if snake bumps to self, loss
            print("You Lost!")
            sys.exit()
    
    def set_field(self, field):
        self.field = field

    def _check_limit(self, point): #checks limit of the field
        if point[0] > self.field.size-1:
            point[0] = 0
        elif point[0] < 0:
            point[0] = self.field.size-1
        elif point[1] < 0:
            point[1] = self.field.size-1
        elif point[1] > self.field.size-1:
            point[1] = 0

    def snake_alive(self):
        head = self.coords[-1]
        snake_body = self.coords[:-1]
        return head not in snake_body #this means snake is still alive
    
    def snake_grow(self):
        # get last point direction
        a = self.coords[0]
        b = self.coords[1]

        tail = a[:]

        if a[0] < b[0]:
            tail[0]-=1
        elif a[1] < b[1]:
            tail[1]-=1
        elif a[0] > b[0]:
            tail[0]+=1
        elif a[1] > b[1]:
            tail[1]+=1

        tail = self._check_limit(tail)
        self.coords.insert(0, tail)