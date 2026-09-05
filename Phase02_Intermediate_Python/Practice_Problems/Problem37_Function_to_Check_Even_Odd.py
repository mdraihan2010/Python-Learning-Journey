# একটি সংখ্যা জোড় নাকি বিজোড় তা check করার function তৈরি করতে হবে।

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))

result = check_even_odd(number)

print("Result:", result)