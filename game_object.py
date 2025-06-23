class GameObject:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]

    def set_position(self, x, y):
        self.position = [x, y]

    def get_position(self):
        return self.position
    
    def direct_move(self, direction):
        if direction == "up":
            self.position[0] -= 1
        elif direction == "down":
            self.position[0] += 1
        elif direction == "left":
            self.position[1] -= 1
        elif direction == "right":
            self.position[1] += 1