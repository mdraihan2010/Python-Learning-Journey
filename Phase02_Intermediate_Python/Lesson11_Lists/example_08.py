# এখন আমরা শিখব একটি List-এ নতুন Element কীভাবে যোগ করতে হয়। 🚀

# 1️⃣ append() Method : append() ব্যবহার করে List-এর শেষে একটি নতুন Element যোগ করা হয়।
# Syntax : list_name.append(value)
# Example:

fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)


# 2️⃣ একাধিক append()

numbers = [10, 20, 30]

numbers.append(40)
numbers.append(50)

print(numbers)


# 3️⃣ insert() Method : insert() ব্যবহার করে নির্দিষ্ট Index-এ নতুন Element যোগ করা যায়।
# Syntax : list_name.insert(index, value)
# Example:

fruits = ["Apple", "Banana", "Mango"]
fruits.insert(1, "Orange")
print(fruits)


# 4️⃣ extend() Method : extend() ব্যবহার করে একটি List-এর সাথে অন্য List-এর একাধিক Element যোগ করা যায়।

numbers1 = [10, 20, 30]
numbers2 = [40, 50]
numbers1.extend(numbers2)
print(numbers1)


# append() → একটি Element যোগ করে
# insert() → নির্দিষ্ট Position-এ Element যোগ করে
# extend() → একাধিক Element যোগ করে