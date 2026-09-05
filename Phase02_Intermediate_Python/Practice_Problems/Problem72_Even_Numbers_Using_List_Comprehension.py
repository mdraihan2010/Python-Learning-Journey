# list comprehension ব্যবহার করে জোড় সংখ্যা তৈরি করো।

n = int(input("Enter N: "))

even_numbers = [number for number in range(1, n + 1) if number % 2 == 0]

print("Even numbers:", even_numbers)