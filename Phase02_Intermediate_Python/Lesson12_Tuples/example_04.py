# Positive Indexing কী? : Python Tuple-এর Index বাম দিক থেকে শুরু হয় এবং প্রথম Element-এর Index হয় 0।

# fruits = ("Apple", "Banana", "Mango", "Orange")

# Index:      0         1         2         3
#             ↓         ↓         ↓         ↓
#           Apple    Banana    Mango     Orange
# এটিই হলো Positive Indexing।


# 1️⃣ প্রথম Element Access করা
fruits = ("Apple", "Banana", "Mango")
print(fruits[0])


# 2️⃣ দ্বিতীয় Element Access করা
fruits = ("Apple", "Banana", "Mango")

print(fruits[1])


# 3️⃣ তৃতীয় Element Access করা
fruits = ("Apple", "Banana", "Mango")
print(fruits[2])


# 4️⃣ Complete Example
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])


# যদি একটি Tuple-এ n টি Element থাকে, তাহলে Positive Index হবে: 0 থেকে n - 1 পর্যন্ত