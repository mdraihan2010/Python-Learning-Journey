# Write a Program to input two integers (a and b) and print:

# All Arithmetic Operations
# All Comparison Operations
# Three Logical Expressions
# Three Bitwise Operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# All Arithmetic Operations
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Exponent =", a ** b)

# All Comparison Operations
print("Equal =", a == b)
print("Not Equal =", a != b)
print("Greater Than =", a > b)
print("Less Than =", a < b)
print("Greater Than or Equal =", a >= b)
print("Less Than or Equal =", a <= b)

# Three Logical Expressions
print("Logical AND =", a > 0 and b > 0)
print("Logical OR =", a > 0 or b > 0)
print("Logical NOT =", not (a == b))

# Three Bitwise Operations
print("Bitwise AND =", a & b)
print("Bitwise OR =", a | b)
print("Bitwise XOR =", a ^ b)