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