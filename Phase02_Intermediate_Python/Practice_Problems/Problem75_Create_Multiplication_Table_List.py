# একটি সংখ্যার multiplication table list আকারে তৈরি করো।

number = int(input("Enter a number: "))

multiplication_table = [number * multiplier for multiplier in range(1, 11)]

print("Multiplication table:", multiplication_table)