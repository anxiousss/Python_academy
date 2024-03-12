class Rectangle:

    def __init__(self, point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2
        self.a = abs(x2 - x1)
        self.b = abs(y2 - y1)
        self.top = max(y1, y2)
        self.left = min(x1, x2)

    def get_pos(self):
        return round(self.left, 2), round(self.top, 2)

    def get_size(self):
        return round(self.a, 2), round(self.b, 2)

    def move(self, dx, dy):
        self.top += dy
        self.left += dx

    def resize(self, width, height):

        self.a, self.b = width, height

    def perimeter(self):

        return round((self.a + self.b) * 2, 2)

    def area(self):

        return round(self.a * self.b, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())

