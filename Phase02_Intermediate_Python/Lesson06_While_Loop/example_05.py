# Multiplication Table using while

number = int(input("Enter a number: "))

value = 1

while value <= 10:
    print(number, "x", value, "=", number * value)
    value = value + 1