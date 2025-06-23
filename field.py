from random import randint

class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ', #the grass where u move
            1: ' * ', #body of snake
            2: ' O ', #head of snake
            3: ' % ', #the apple
        }
        self.snake_coords = []

    def add_entity(self):
        
        while True:
            i = randint(0, self.size-1)
            j = randint(0, self.size-1)
            entity = [i, j]
            
            if entity not in self.snake_coords:
                self.field[i][j] = 3
                break
    
    def _generate_field(self):
        self.field = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def _clear_field(self):        
        self.field = [[j if j!= 1 and j!= 2 else 0 for j in i] for i in self.field]

    def render(self, screen):
        size = self.size
        self._clear_field()

        for i, j in self.snake_coords: #render snake on the field
            self.field[i][j] = 1

        head = self.snake_coords[-1] #marks head
        self.field[head[0]][head[1]] = 2

        for i in range(self.size):
            row = ''
            for j in range(self.size):
                row += self.icons[self.field[i][j]]
            screen.addstr(i, 0, row)