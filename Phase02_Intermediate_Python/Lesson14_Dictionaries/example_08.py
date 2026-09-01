# এখন আমরা শিখব Dictionary-এর Key, Value এবং Key-Value Pair Loop করে কীভাবে Access করতে হয়। 🚀

student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.75
}



# 1️⃣ শুধু Keys-এর উপর Loop
for key in student:
    print(key)



# 2️⃣ keys() ব্যবহার করে
for key in student.keys():
    print(key)



# 3️⃣ শুধু Values-এর উপর Loop : values() ব্যবহার করে শুধু Value পাওয়া যায়।

for value in student.values():
    print(value)



# 4️⃣ Key এবং Value একসাথে Loop করা ⭐ : items() ব্যবহার করলে Key এবং Value দুটোই একসাথে পাওয়া যায়।
for key, value in student.items():
    print(key, "=", value)



# 5️⃣ Condition ব্যবহার করে Dictionary Loop
# ধরো আমরা শুধু যেসব Student-এর CGPA 3.50 বা তার বেশি তাদের বের করতে চাই।
students = {
    "Raihan": 3.75,
    "Rahim": 3.20,
    "Karim": 3.60,
    "Hasan": 3.10
}
for name, cgpa in students.items():
    if cgpa >= 3.50:
        print(name, cgpa)



# 6️⃣ Dictionary থেকে শুধু নির্দিষ্ট Value Print
student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.75
}
for key, value in student.items():
    if key == "cgpa":
        print("CGPA =", value)



# 7️⃣ Nested Dictionary Loop
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

# Outer Dictionary Loop:
for student_id, information in students.items():
    print(student_id)
    print(information)

# Nested Dictionary-এর ভিতরের Value Access করতেও পারি:
for student_id, information in students.items():
    print("Name =", information["name"])
    print("CGPA =", information["cgpa"])


# সহজভাবে মনে রাখো:

# keys() → Key
# values() → Value
# items() → Key + Value