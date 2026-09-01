# এখন আমরা শিখব Dictionary থেকে Key-Value Pair কীভাবে Remove বা Delete করতে হয়। 🚀

# Dictionary থেকে Item Remove করার জন্য কয়েকটি গুরুত্বপূর্ণ উপায় আছে:
# 1. pop()
# 2. popitem()
# 3. del
# 4. clear()



# 1️⃣ pop() Method : pop() ব্যবহার করে নির্দিষ্ট Key এবং তার Value Remove করা যায়।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
student.pop("age")
print(student)

# Output: {'name': 'Raihan', 'cgpa': 3.75}
# এখানে "age": 23 পুরো Key-Value Pair-টি Remove হয়েছে।

# pop() Removed Value Return করে
student = {
    "name": "Raihan",
    "age": 23
}
removed_value = student.pop("age")
print("Removed Value =", removed_value)
print(student)

# Output:
# Removed Value = 23
# {'name': 'Raihan'}



# 2️⃣ popitem() Method : popitem() Dictionary-এর শেষের Key-Value Pair Remove করে।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
student.popitem()
print(student)

# ⚠️ popitem()-এ কোন Key দিতে হয় না।




# 3️⃣ del Keyword : del ব্যবহার করে নির্দিষ্ট Key-Value Pair Delete করা যায়।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
del student["age"]
print(student)

# পুরো Dictionary Delete করা
student = {
    "name": "Raihan",
    "age": 23
}
del student



# 4️⃣ clear() Method :clear() Dictionary-এর সব Key-Value Pair Remove করে।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
student.clear()
print(student)

# 🧠 pop() vs popitem() vs del vs clear()
# pop("key")
# → নির্দিষ্ট Key Remove করে

# popitem()
# → শেষ Key-Value Pair Remove করে

# del dictionary["key"]
# → নির্দিষ্ট Key Delete করে

# clear()
# → সব Key-Value Pair Remove করে


# একটি ছোট Example:
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
student.pop("age")
student.popitem()
print(student)