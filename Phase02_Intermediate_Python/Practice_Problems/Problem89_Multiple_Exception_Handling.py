# একাধিক ধরনের exception handle করো।

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = first_number / second_number

    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")