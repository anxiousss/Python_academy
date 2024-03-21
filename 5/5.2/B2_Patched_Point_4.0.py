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
        dist = round((x_dist ** 2 + y_dist ** 2) ** 0.5, 2)
        return dist


class PatchedPoint(Point):

    def __init__(self, *args):

        if not args:
            self.x = 0
            self.y = 0
            super().__init__(self.x, self.y)

        elif len(args) == 1:
            self.x, self.y = args[0]
            super().__init__(self.x, self.y)

        else:
            self.x, self.y = args[0], args[1]
            super().__init__(self.x, self.y)

    def __repr__(self):

        return f'PatchedPoint({self.x}, {self.y})'

    def __str__(self):

        return f'({self.x}, {self.y})'

