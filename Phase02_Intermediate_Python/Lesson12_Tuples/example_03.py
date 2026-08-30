# এখন আমরা শিখব Tuple-এর ভিতরে থাকা নির্দিষ্ট Element কীভাবে Access করতে হয়। 🚀

# fruits = ("Apple", "Banana", "Mango", "Orange")

# Tuple-এর প্রতিটি Element-এর একটি Index Number থাকে।
# Index:      0         1         2         3
#             ↓         ↓         ↓         ↓
#           Apple    Banana    Mango     Orange


# 1️⃣ প্রথম Element Access করা
fruits = ("Apple", "Banana", "Mango")
print(fruits[0])


# 2️⃣ বিভিন্ন Element Access করা
fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# 3️⃣ Number Tuple থেকে Element Access করা
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[2])
print(numbers[4])


# 4️⃣ Variable ব্যবহার করে Index Access করা
fruits = ("Apple", "Banana", "Mango")
index = 1
print(fruits[index])

# 5️⃣ Nested Tuple থেকে Element Access করা
numbers = (1, 2, (3, 4), 5)
print(numbers[2])

# এখন Inner Tuple-এর Element Access করতে:

print(numbers[2][0])
print(numbers[2][1])


# 6️⃣ Index-এর বাইরে গেলে কী হবে? ⚠️
# fruits = ("Apple", "Banana", "Mango")
# print(fruits[5])

# তাহলে Error হবে: IndexError: tuple index out of range . কারণ Tuple-এ মাত্র 3টি Element আছে।
# তাদের Index হলো:  0 → Apple
#                    1 → Banana
#                    2 → Mango
# কিন্তু Index 5 নেই।













