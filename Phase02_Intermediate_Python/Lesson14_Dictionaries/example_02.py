# এখন আমরা Python-এ বিভিন্নভাবে Dictionary তৈরি করা শিখব। 🚀
# Dictionary-এর Basic Structure:
# dictionary = {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }



# 1️⃣ সাধারণভাবে Dictionary তৈরি করা : {} ব্যবহার করে Key-Value Pair লিখে Dictionary তৈরি করা যায়।
from multiprocessing import Value


student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.75
}
print(student)



# 2️⃣ Empty Dictionary : খালি Dictionary তৈরি করতে:
student = {}
print(student)

# ⚠️ মনে রাখবে:
# {}      → Empty Dictionary
# set()   → Empty Set


# 3️⃣ dict() Function ব্যবহার করে : Dictionary তৈরির আরেকটি উপায় হলো dict()।
student = dict(
    name="Raihan",
    age=23,
    department="CSE"
)
print(student)



# 4️⃣ List of Tuples থেকে Dictionary
student = dict([
    ("name", "Raihan"),
    ("age", 23),
    ("cgpa", 3.75)
])
print(student)

# প্রতিটি Tuple-এর প্রথম Element হলো Key এবং দ্বিতীয়টি হলো Value।
# ("name", "Raihan")
#     ↑          ↑
#    Key       Value



# 5️⃣ Dictionary-এর Value বিভিন্ন Data Type হতে পারে
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75,
    "is_student": True
}
print(student)

# একটি Dictionary-এর Value হতে পারে:
# String
# Integer
# Float
# Boolean



# 6️⃣ List-কে Value হিসেবে রাখা : Dictionary-এর Value হিসেবে List রাখা যায়।
student = {
    "name": "Raihan",
    "subjects": ["Python", "Math", "Physics"]
}
print(student)



# 7️⃣ Dictionary-এর ভিতরে Dictionary : এটাকে Nested Dictionary বলে।
students = {
    "student1": {
        "name": "Raihan",
        "cgpa": 3.75
    },
    "student2": {
        "name": "Rahim",
        "cgpa": 3.50
    }
}
print(students)