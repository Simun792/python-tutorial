"""
1. Inheritence
2. Abstract class and method initialization in parent and implementation in child
3. Method overriding (Changing parent class method code in child class method)
"""

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type, width=None, height=None, radius=None) -> None:
        print("Shape initialized for", shape_type)
        self.shape_type = shape_type
        self.width = width
        self.height = height
        self.radius = radius

    def get_all_parameters(self):
        print("Shape Type", self.shape_type)
        print("Width", self.width)
        print("Height", self.height)
        print("Radius", self.radius)
        print()


    def number_of_lines(self):
        print("Number lines is 0")

    @abstractmethod #decorator
    def get_perimeter(self):
        pass


class Circle(Shape):
    def get_area(self):
        area = math.pi * self.radius ** 2
        return area

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def number_of_lines(self):
        print("Number lines is 1")


class rectangle(Shape):
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def number_of_lines(self):
        print("Number lines is 4")
    


c = Circle(shape_type="Circle", radius=4)
c.get_all_parameters()
area = c.get_area()
print(f"Area of circle is {area}")
perimeter = c.get_perimeter()
print(f"Perimeter of circle is {perimeter}")
print(c.number_of_lines())

print()

c = rectangle(shape_type="Rectangle", height=4, width=6)
c.get_all_parameters()
area = c.get_area()
print(f"Area of rectangle is {area}")
perimeter = c.get_perimeter()
print(f"Perimeter of rectangle is {perimeter}")
print(c.number_of_lines())