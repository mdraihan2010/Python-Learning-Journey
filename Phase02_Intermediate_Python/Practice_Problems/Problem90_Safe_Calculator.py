# exception handling ব্যবহার করে একটি safe calculator তৈরি করো।

try:
    first_number = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second_number = float(input("Enter second number: "))

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    else:
        result = "Invalid operator"

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")