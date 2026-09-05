# list comprehension ব্যবহার করে বিজোড় সংখ্যা তৈরি করো।

n = int(input("Enter N: "))

odd_numbers = [number for number in range(1, n + 1) if number % 2 != 0]

print("Odd numbers:", odd_numbers)