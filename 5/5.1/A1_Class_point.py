class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return self.x, self.y


point = Point(2, -7)
print(point.x, point.y)

