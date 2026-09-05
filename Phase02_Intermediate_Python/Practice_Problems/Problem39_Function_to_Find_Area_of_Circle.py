# বৃত্তের area বের করার function তৈরি করতে হবে।

def find_circle_area(radius):
    pi = 3.1416
    return pi * radius ** 2


radius = float(input("Enter the radius of the circle: "))

area = find_circle_area(radius)

print("Area of the circle:", area)