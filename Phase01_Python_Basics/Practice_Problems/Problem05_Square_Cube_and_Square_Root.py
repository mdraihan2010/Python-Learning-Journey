# Write a Program to input a number and print its square, cube, and square root.

number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3

# For square root, we can use the exponent 0.5 
 
square_root = number ** 0.5

print("Square =", int(square))
print("Cube =", int(cube))
print("Square Root =", round(square_root, 2))