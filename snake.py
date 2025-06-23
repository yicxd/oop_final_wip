from game_object import GameObject
import curses

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

        #new updating coords of the head
        if self.direction == curses.KEY_UP:
            head[0]-=1
        elif self.direction == curses.KEY_DOWN:
            head[0]+=1
        elif self.direction == curses.KEY_RIGHT:
            head[1]+=1
        elif self.direction == curses.KEY_LEFT:
            head[1]-=1