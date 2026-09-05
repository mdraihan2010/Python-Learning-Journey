# recursion ব্যবহার করে factorial বের করতে হবে।

def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


n = int(input("Enter a number: "))

result = factorial(n)

print("Factorial:", result)