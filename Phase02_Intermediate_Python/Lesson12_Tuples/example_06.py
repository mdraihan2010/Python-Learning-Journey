# Tuple Slicing কী? : Tuple-এর একটি নির্দিষ্ট অংশ বা একাধিক Element একসাথে Access করাকে Tuple Slicing বলে।

# Basic Syntax : tuple_name[start : stop]

# এখানে:
# start → কোন Index থেকে শুরু হবে
# stop → কোন Index-এর আগে শেষ হবে

# সবচেয়ে গুরুত্বপূর্ণ বিষয়: Start Index Include হয়, কিন্তু Stop Index Include হয় না।


fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[1:4])


# 1️⃣ Start না দিলে যদি Tuple-এর শুরু থেকে Slice করতে চাও:
numbers = (10, 20, 30, 40, 50)
print(numbers[:3])


# 2️⃣ Stop না দিলে
numbers = (10, 20, 30, 40, 50)
print(numbers[2:])


# 3️⃣ পুরো Tuple Slice করা
numbers = (10, 20, 30, 40, 50)
print(numbers[:])


# 4️⃣ Negative Index ব্যবহার করে Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[-4:-1])


# 5️⃣ Step ব্যবহার করে Slicing
# Tuple Slicing-এর সম্পূর্ণ Syntax: tuple_name[start : stop : step]
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[0:6:2])


# আরও সহজভাবে
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[::2])


# 6️⃣ Tuple Reverse করা : Slicing ব্যবহার করে Tuple Reverse করা যায়।
numbers = (10, 20, 30, 40, 50)
print(numbers[::-1])

