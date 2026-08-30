# এখন আমরা শিখব Tuple-এ নতুন Element কীভাবে যোগ করা যায়। 🚀


# 1️⃣ একটি Element যোগ করা : Tuple-এর সাথে নতুন Tuple যোগ করতে + Operator ব্যবহার করা যায়।
fruits = ("Apple", "Banana", "Mango")
fruits = fruits + ("Orange",)
print(fruits)


# ⚠️ Comma না দিলে এটি Tuple হবে না।
# এটি: ("Orange")
# একটি String হিসেবে ধরা হবে।
# কিন্তু: ("Orange",)
# এটি একটি Tuple।
# তাই নতুন একটি মাত্র Element যোগ করার সময় Comma দিতে হবে।


# 2️⃣ একাধিক Element যোগ করা
fruits = ("Apple", "Banana")
fruits = fruits + ("Mango", "Orange")
print(fruits)



# 3️⃣ List ব্যবহার করে Element যোগ করা : আগের মতো Tuple-কে List-এ Convert করেও নতুন Element যোগ করা যায়।

fruits = ("Apple", "Banana", "Mango")
fruits_list = list(fruits)
fruits_list.append("Orange")
fruits = tuple(fruits_list)
print(fruits)
