# *args ব্যবহার করে একাধিক সংখ্যার যোগফল বের করতে হবে।

def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

result = calculate_sum(number1, number2, number3)

print("Sum:", result)