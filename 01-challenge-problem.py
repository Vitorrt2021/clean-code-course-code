class Point:
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


class Rectangle:
    def __init__(self, origin, width, heigth):
        self.origin = origin
        self.width = width
        self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth

    def print_vertex(self):
        top_right = self.origin.coordinate_x + self.width
        bottom_left = self.origin.coordinate_y + self.heigth
        print('Starting Point (X)): ' + str(self.origin.coordinate_x))
        print('Starting Point (Y)): ' + str(self.origin.coordinate_y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_retangle():
    origin = Point(50, 100)
    rect = Rectangle(origin, 90, 10)
    return rect


rectangle = build_retangle()

print(rectangle.area())
rectangle.print_vertex()
