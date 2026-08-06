#Operator Precedence

# P → Parentheses ()
# E → Exponent **
# MD → Multiplication, Division (*, /, //, %)
# AS → Addition, Subtraction (+, -)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result1 = a + b * 2
print("Result 1 =", result1)

result2 = (a + b) * 2
print("Result 2 =", result2)