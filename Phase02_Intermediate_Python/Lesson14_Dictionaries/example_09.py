# এখন আমরা শিখব একটি Dictionary-এর ভিতরে আরেকটি Dictionary কীভাবে রাখা ও ব্যবহার করা যায়। 🚀

# Nested Dictionary কী? : একটি Dictionary-এর Value হিসেবে আরেকটি Dictionary থাকলে তাকে Nested Dictionary বলে।
# Access করার Pattern: outer_dictionary[outer_key][inner_key]

students = {
    "student1": {
        "name": "Raihan",
        "age": 23,
        "cgpa": 3.75
    },
    "student2": {
        "name": "Rahim",
        "age": 22,
        "cgpa": 3.50
    }
}
print(students)

# এখানে students হলো একটি Dictionary এবং এর ভিতরে student1 ও student2 নামে আরও দুটি Dictionary আছে।



# 1️⃣ Nested Dictionary Access করা
# প্রথম Student-এর পুরো Information:
print(students["student1"])

# শুধু Name:
print(students["student1"]["name"])

# শুধু CGPA:
print(students["student1"]["cgpa"])

# এখানে:
# students["student1"]          → Inner Dictionary
# students["student1"]["name"]  → Inner Dictionary-এর Value



# 2️⃣ Nested Dictionary Update করা
students["student1"]["cgpa"] = 3.90
print(students["student1"])



# 3️⃣ নতুন Item যোগ করা
students["student1"]["department"] = "CSE"
print(students["student1"])



# 4️⃣ Nested Dictionary Loop করা
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
for student_id, information in students.items():

    print("Student ID:", student_id)
    print("Name:", information["name"])
    print("CGPA:", information["cgpa"])



# 5️⃣ Real-Life Example 🎓 : একাধিক Student-এর Information Store করতে Nested Dictionary খুব Useful।
students = {
    "101": {
        "name": "Raihan",
        "department": "CSE",
        "cgpa": 3.75
    },
    "102": {
        "name": "Rahim",
        "department": "EEE",
        "cgpa": 3.50
    },
    "103": {
        "name": "Karim",
        "department": "CE",
        "cgpa": 3.60
    }
}

# এখন Student 101-এর Department:
# print(students["101"]["department"])

# Student 103-এর CGPA:
# print(students["103"]["cgpa"])

# 🧠 Structure মনে রাখো
# students
#    │
#    ├── student1
#    │      ├── name
#    │      ├── age
#    │      └── cgpa
#    │
#    └── student2
#           ├── name
#           ├── age
#           └── cgpa
