class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return self.x, self.y

    def move(self, x, y):
        self.x = x + self.x
        self.y = y + self.y
        return self.x, self.y

    def length(self, other_point):
        x2, y2 = other_point.coordinates()
        x_dist = x2 - self.x
        y_dist = y2 - self.y
        dist = round((x_dist**2 + y_dist**2)**0.5, 2)
        return dist


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
