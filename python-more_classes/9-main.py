#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

r1 = Rectangle(45,23)
print(r1)
print(f"\tRectangle: {r1.area()}, Perimeter : {r1.perimeter()}")