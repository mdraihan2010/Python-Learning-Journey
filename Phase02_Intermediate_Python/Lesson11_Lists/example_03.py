# এখন আমরা শিখব List-এর ভিতরে থাকা নির্দিষ্ট Item কীভাবে Access করতে হয়। 🚀


fruits = ["Apple", "Banana", "Mango", "Orange"]


# প্রতিটি Item-এর একটি Index Number থাকে।
# Index:    0         1         2        3
#           ↓         ↓         ↓        ↓
#         Apple    Banana     Mango    Orange
# ⚠️ Python-এ Index শুরু হয় 0 থেকে।

# Basic Access

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# Mixed Data Type List Access

student = ["Raihan", 23, "CSE", 3.75]

print(student[0])
print(student[1])
print(student[2])
print(student[3])


# Nested List থেকে Element Access

numbers = [1, 2, [3, 4], 5]

print(numbers[2])