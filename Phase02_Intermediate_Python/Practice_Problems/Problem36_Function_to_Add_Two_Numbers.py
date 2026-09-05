# দুটি সংখ্যা যোগ করার function তৈরি করতে হবে।

def add_numbers(num1, num2):
    return num1 + num2


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

result = add_numbers(number1, number2)

print("Sum:", result)