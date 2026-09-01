# Dictionary কী? : Dictionary হলো একটি Collection যেখানে Data Key : Value Pair আকারে Store করা হয়।

# 1️⃣ Dictionary কীভাবে লেখা হয়? : Dictionary তৈরি করতে {} ব্যবহার করা হয়।
student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE"
}
print(student)


# প্রতিটি Key এবং Value-এর মাঝে : থাকে।
# "name": "Raihan"
#   ↑         ↑
#  Key      Value
# আর প্রতিটি Pair-এর মাঝে , থাকে।



# 2️⃣ Dictionary-তে Duplicate Key রাখা যায় না ⚠️
student = {
    "name": "Raihan",
    "age": 23,
    "name": "Rahim"
}
print(student)

# এখানে "name" দুইবার দেওয়া হয়েছে।
# Python শেষের Value-টি রাখবে: {'name': 'Rahim', 'age': 23}
# তাই: Dictionary-এর Key Unique হতে হবে।



# 3️⃣ Dictionary-তে Duplicate Value থাকতে পারে
students = {
    "student1": "Raihan",
    "student2": "Raihan"
}
print(students)

# এখানে Value "Raihan" দুইবার আছে, এবং এটি কোনো সমস্যা নয়।



# 4️⃣ Dictionary Ordered : আধুনিক Python-এ Dictionary যে Order-এ Item যোগ করা হয়, সেই Insertion Order সংরক্ষিত থাকে।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.75
}
print(student)

# তবে Dictionary-কে List-এর মতো Index দিয়ে Access করা হয় না।

# 5️⃣ Dictionary-তে Index নেই
# List:
numbers = [10, 20, 30]
print(numbers[0])

# কিন্তু Dictionary:
student = {
    "name": "Raihan",
    "age": 23
}
print(student[0])

# এভাবে Access করা ঠিক নয়। Dictionary-তে Key ব্যবহার করে Value Access করা হয়।
print(student["name"])



# 6️⃣ Dictionary Mutable : Dictionary তৈরি করার পর এর Value পরিবর্তন করা যায় এবং নতুন Key-Value Pair যোগ করা যায়।
student = {
    "name": "Raihan",
    "age": 23
}
student["age"] = 24
print(student)

