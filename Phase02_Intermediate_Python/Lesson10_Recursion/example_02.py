# Factorial Using Recursion 

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)


number = int(input("Enter the number: "))

result = factorial(number)

print("Factorial =", result)