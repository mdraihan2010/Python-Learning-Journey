# এখন আমরা শিখব Dictionary-এর Value কীভাবে Access করতে হয়। 🚀

student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.75
}

# Dictionary-তে List-এর মতো Index ব্যবহার করা হয় না। এখানে Key ব্যবহার করে Value Access করা হয়।



# 1️⃣ Square Brackets [] ব্যবহার করে
print(student["name"])
# আর:
print(student["cgpa"])

# অর্থাৎ:
# student["name"]       → "Raihan"
# student["age"]        → 23
# student["department"] → "CSE"
# student["cgpa"]       → 3.75



# 2️⃣ .get() Method ব্যবহার করে  : Dictionary Value Access করার আরেকটি উপায় হলো get()।
print(student.get("name"))


# দুটোই কাজ করে:
# student["name"]
# এবং:
# student.get("name")
# ⚠️ [] এবং get()-এর পার্থক্য

# যদি Dictionary-তে এমন Key থাকে:

print(student["phone"])

# তাহলে Error হবে:
# KeyError: 'phone'
# কিন্তু:
# print(student.get("phone"))
# Output হবে:
# None
# তাই Key আছে কি না নিশ্চিত না হলে get() বেশি নিরাপদ।



# 3️⃣ get()-এ Default Value দেওয়া : চাইলে Key না থাকলে নিজের একটি Default Value দেখাতে পারো।

print(student.get("phone", "Not Available"))



# 4️⃣ Variable ব্যবহার করে Access
key = "department"
print(student[key])



# 5️⃣ Nested Dictionary Access
students = {
    "student1": {
        "name": "Raihan",
        "cgpa": 3.75
    }
}

# প্রথমে student1 Access:
print(students["student1"])

# Output: {'name': 'Raihan', 'cgpa': 3.75}

# তারপর ভিতরের name:
print(students["student1"]["name"])

# Output: Raihan

# এবং:
print(students["student1"]["cgpa"])

# Output: 3.75


# 🧠 মনে রাখো
# List/Tuple
# → Index দিয়ে Access

# Dictionary
# → Key দিয়ে Access