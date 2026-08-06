# Write a Program to input your name, age, university, department, CGPA, and two favorite numbers. Then print your personal information, perform all Arithmetic Operations on the two numbers, compare them using Comparison Operators, evaluate Logical expressions, and display the results of Bitwise AND, OR, and XOR.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
department = input("Enter your department: ")
CGPA = float(input("Enter your CGPA: "))
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))

print("\nPersonal Information:")
print("Name:", name)
print("Age:", age)
print("University:", university)
print("Department:", department)
print("CGPA:", CGPA)

print("\nArithmetic Operations:")
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Exponent =", num1 ** num2)

print("\nComparison Operations:")
print("Equal =", num1 == num2)
print("Not Equal =", num1 != num2)
print("Greater Than =", num1 > num2)
print("Less Than =", num1 < num2)
print("Greater Than or Equal =", num1 >= num2)
print("Less Than or Equal =", num1 <= num2)

print("\nLogical Expressions:")
print("Logical AND =", num1 > 0 and num2 > 0)
print("Logical OR =", num1 > 0 or num2 > 0)
print("Logical NOT =", not (num1 == num2))

print("\nBitwise Operations:")
print("Bitwise AND =", num1 & num2)
print("Bitwise OR =", num1 | num2)
print("Bitwise XOR =", num1 ^ num2)

