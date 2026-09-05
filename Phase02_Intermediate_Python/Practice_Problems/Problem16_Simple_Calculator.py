# +, -, *, / ব্যবহার করে একটি calculator তৈরি করতে হবে।


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        result = num1 + num2
        print("Result:", result)

    case "-":
        result = num1 - num2
        print("Result:", result)

    case "*":
        result = num1 * num2
        print("Result:", result)

    case "/":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Cannot divide by zero")

    case _:
        print("Invalid operator")