class Field:
    def __init__(self, size):
        self.size = size
        self.icons = {
            0: ' . ', #the grass where u move
            1: ' * ', #body of snake
            2: ' O ', #head of snake
            3: ' % ', #the apple
        }