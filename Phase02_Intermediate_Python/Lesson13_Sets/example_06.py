# এখন আমরা Set-এর কিছু গুরুত্বপূর্ণ Method একসাথে শিখব। 🚀


# 1️⃣ copy() : একটি Set-এর Copy তৈরি করতে ব্যবহার করা হয়।
numbers = {10, 20, 30}
new_numbers = numbers.copy()
print(new_numbers)



# 2️⃣ difference() : একটি Set-এ থাকা কিন্তু অন্য Set-এ না থাকা Element বের করে।

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.difference(set2)
print(result)

# এটি এভাবেও লেখা যায়: set1 - set2



# 3️⃣ intersection() : দুইটি Set-এর Common Element বের করে।
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.intersection(set2)
print(result)

# এটি এভাবেও লেখা যায়: set1 & set2



# 4️⃣ union() : দুইটি Set-এর সব Unique Element একসাথে করে।
set1 = {10, 20, 30}
set2 = {30, 40, 50}
result = set1.union(set2)
print(result)

# এটি এভাবেও লেখা যায়: set1 | set2



# 5️⃣ isdisjoint()দুইটি Set-এর মধ্যে কোনো Common Element আছে কি না Check করে।
set1 = {10, 20, 30}
set2 = {40, 50, 60}
print(set1.isdisjoint(set2))


# আর:
set1 = {10, 20, 30}
set2 = {30, 40, 50}
print(set1.isdisjoint(set2))