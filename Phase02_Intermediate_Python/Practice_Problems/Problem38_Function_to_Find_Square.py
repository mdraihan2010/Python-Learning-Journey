# একটি সংখ্যার square বের করার function তৈরি করতে হবে।

def find_square(number):
    return number ** 2


number = float(input("Enter a number: "))

result = find_square(number)

print("Square:", result)