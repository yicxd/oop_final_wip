class GameObject:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]

    def set_position(self, x, y):
        self.position = [x, y]

    def get_position(self):
        return self.position