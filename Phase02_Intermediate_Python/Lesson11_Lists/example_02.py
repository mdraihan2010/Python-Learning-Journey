# Python-এ বিভিন্নভাবে List তৈরি করা। 🚀

# 1️⃣ Square Brackets ব্যবহার করে List তৈরি : List তৈরি করার সবচেয়ে সাধারণ উপায় হলো [] ব্যবহার করা।

fruits = ["Apple", "Banana", "Mango"]
print(fruits)


# 2️⃣ Number List

numbers = [10, 20, 30, 40, 50]
print(numbers)


# 3️⃣ String List

names = ["Raihan", "Rahim", "Karim"]
print(names)


# 4️⃣ Different Data Types দিয়ে List : একটি List-এর মধ্যে বিভিন্ন ধরনের Data রাখা যায়।

student = ["Raihan", 23, 3.75, True]
print(student)

# এখানে:
# "Raihan" → String
# 23       → Integer
# 3.75     → Float
# True     → Boolean


# 5️⃣ Empty List : কোনো Item ছাড়া List তৈরি করতে:

numbers = []
print(numbers)


# 6️⃣ Duplicate Value সহ List : List একই Value একাধিকবার Store করতে পারে।

numbers = [10, 20, 10, 30, 20]
print(numbers)


# 7️⃣ Nested List : একটি List-এর ভিতরে আরেকটি List থাকতে পারে।

numbers = [1, 2, [3, 4], 5]
print(numbers)


# 8️⃣ list() Function ব্যবহার করে List তৈরি

numbers = list((10, 20, 30))
print(numbers)

