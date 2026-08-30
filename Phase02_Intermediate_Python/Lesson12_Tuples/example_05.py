# Negative Indexing কী?
# Positive Indexing বাম দিক থেকে শুরু হয়: 0 → 1 → 2 → 3
# আর Negative Indexing ডান দিক থেকে শুরু হয়: -4 → -3 → -2 → -1

# fruits = ("Apple", "Banana", "Mango", "Orange")

# Ptive Index:      0         1         2         3
#                   ↓         ↓         ↓         ↓
#                 Apple    Banana    Mango     Orange
#                   ↑         ↑         ↑         ↑
# Negative Index:  -4        -3        -2        -1

# সবচেয়ে গুরুত্বপূর্ণ বিষয়: শেষ Element-এর Negative Index সবসময় -1।


# 1️⃣ শেষ Element Access করা
fruits = ("Apple", "Banana", "Mango")
print(fruits[-1])



# 2️⃣ অন্যান্য Element Access করা
fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])



# 3️⃣ Number Tuple Example
numbers = (10, 20, 30, 40, 50)
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])



# 4️⃣ Nested Tuple-এ Negative Indexing
numbers = (1, 2, (3, 4), 5)
print(numbers[-1])

# Inner Tuple-এর শেষ Element Access করতে:
print(numbers[-2][-1])


# 5️⃣ Index-এর বাইরে গেলে ⚠️
numbers = (10, 20, 30)

print(numbers[-4])

# তাহলে Error হবে: IndexError: tuple index out of range. কারণ Tuple-এ মাত্র 3টি Element আছে।


# Positive Indexing → বাম দিক থেকে শুরু → 0
# Negative Indexing → ডান দিক থেকে শুরু → -1