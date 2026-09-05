# list comprehension ব্যবহার করে ১ থেকে N পর্যন্ত square তৈরি করো।

n = int(input("Enter N: "))

squares = [number ** 2 for number in range(1, n + 1)]

print("Squares:", squares)