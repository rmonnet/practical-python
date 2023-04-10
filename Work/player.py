# An example of python class

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, points):
        self.health -= points


a = Player(2, 3)
b = Player(10, 20)

print(f'a.x={a.x}')
