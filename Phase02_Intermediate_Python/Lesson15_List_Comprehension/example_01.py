# 📖 1. List Comprehension কী? : সাধারণভাবে কোনো list থেকে নতুন list তৈরি করতে আমরা for loop ব্যবহার করি।
# Basic Syntax  : [expression for item in iterable]

# এখানে—
# expression → কী value list-এ রাখব
# item → একেকটি element
# iterable → list, tuple, range, string ইত্যাদি


# Normal for loop:

numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)


# একই কাজ List Comprehension দিয়ে:

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)


# range() এর সাথে List Comprehension
numbers = [number for number in range(1, 6)]
print(numbers)


# List Comprehension with Calculation
numbers = [10, 20, 30, 40]
result = [number + 5 for number in numbers]
print(result)


# String-এর উপর List Comprehension
name = "Python"
letters = [letter for letter in name]
print(letters)
