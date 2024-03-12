class Rectangle:

    def __init__(self, point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2
        self.a = abs(x2 - x1)
        self.b = abs(y2 - y1)

    def perimeter(self):

        return round((self.a + self.b) * 2, 2)

    def area(self):

        return round(self.a * self.b, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())

