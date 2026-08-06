# Write a Program to input the side of a square, the length and width of a rectangle, the radius of a circle, and the base and height of a triangle. Print the area of each shape.Lesson Readme.md format


side = float(input("Enter the side of the square: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Area of Square
area_square = side ** 2

# Area of Rectangle
area_rectangle = length * width

# Area of Circle
area_circle = 3.14 * radius ** 2

# Area of Triangle
area_triangle = (base * height) / 2

print("Area of Square =", int(area_square))
print("Area of Rectangle =", int(area_rectangle))
print("Area of Circle =", round(area_circle, 2))
print("Area of Triangle =", int(area_triangle))
