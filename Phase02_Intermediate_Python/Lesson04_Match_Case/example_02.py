operator = input("Enter an operator (+, -, *, /): ")

match operator:
    case "+":
        print("Addition")

    case "-":
        print("Subtraction")

    case "*":
        print("Multiplication")

    case "/":
        print("Division")

    case _:
        print("Invalid operator")