class Rectangle:
    def __init__(self, point1, point2):
        self.left = min(point1[0], point2[0])
        self.top = max(point1[1], point2[1])
        self.right = max(point1[0], point2[0])
        self.bottom = min(point1[1], point2[1])
        self.width = round(abs(point1[0] - point2[0]), 2)
        self.height = round(abs(point1[1] - point2[1]), 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.left, self.top

    def get_size(self):
        return self.width, self.height

    def resize(self, width, height):
        self.right = self.left + width
        self.bottom = self.top - height
        self.width = width
        self.height = height

    def turn(self):
        center_x = (self.left + self.right) / 2
        center_y = (self.top + self.bottom) / 2
        new_width = self.height
        new_height = self.width
        half_width = new_width / 2
        half_height = new_height / 2
        self.left = center_x - half_width
        self.right = center_x + half_width
        self.top = center_y + half_height
        self.bottom = center_y - half_height
        self.width = new_width
        self.height = new_height

    def scale(self, factor):
        center_x = (self.left + self.right) / 2
        center_y = (self.top + self.bottom) / 2
        new_width = round(self.width * factor, 2)
        new_height = round(self.height * factor, 2)
        half_width = new_width / 2
        half_height = new_height / 2
        self.left = center_x - half_width
        self.right = center_x + half_width
        self.top = center_y + half_height
        self.bottom = center_y - half_height
        self.width = new_width
        self.height = new_height
        