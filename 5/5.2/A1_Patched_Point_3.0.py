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


class PatchedPoint(Point):

    def __init__(self, *args):
        
        if not args:
            super().__init__(x=0, y=0)

        elif len(args) == 1:
            x, y = args[0]
            super().__init__(x, y)

        else:
            x, y = args[0], args[1]
            super().__init__(x, y)

        
