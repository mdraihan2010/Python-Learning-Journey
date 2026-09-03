# এখন আমরা নিজেরা Module এবং Package তৈরি করে একটি ছোট Project বানাব। 🚀
# আজকের Project-এর নাম: Student Management System 🎓
# এই Project-এ আমরা আলাদা আলাদা File-এ Function রাখব এবং main.py থেকে সেগুলো Import করে ব্যবহার করব।



# 1️⃣ Project-এর Folder Structure -> প্রথমে একটি Folder তৈরি করো:

# Student_Project/
# │
# ├── main.py
# │
# ├── student.py
# │
# └── utilities/
#     ├── __init__.py
#     └── calculator.py

# এখানে:
# main.py       → Main Program
# student.py    → Student Module
# utilities     → Package
# calculator.py → Package-এর ভিতরের Module

# ⚠️ calculator.py এবং main.py আলাদা File হবে।
# একটি File-এর Code অন্য File-এর মধ্যে লিখবে না।

# 2️⃣ student.py Module তৈরি করা : 
# student.py File-এর মধ্যে লিখো:

name = "Raihan"
age = 23
department = "CSE"
def introduce():
    print("My name is", name)
    print("Age:", age)
    print("Department:", department)
def is_adult():
    return age >= 18

# এখানে আমরা তৈরি করেছি:
# 3টি Variable
# 2টি Function



# 3️⃣ main.py থেকে student.py Import করা
# এখন main.py File-এ লিখো:

# import student
# print(student.name)
# print(student.age)
# print(student.department)
# student.introduce()
# print("Adult:", student.is_adult())

# এখানে:
# student.name
# মানে student.py Module-এর name Variable ব্যবহার করা হয়েছে।
# আর:
# student.introduce()
# মানে student.py Module-এর introduce() Function Call করা হয়েছে।

# 4️⃣ utilities Package তৈরি করা
# এখন utilities Folder-এর ভিতরে দুটি File তৈরি করো:
# utilities/
# │
# ├── __init__.py
# └── calculator.py
# __init__.py File আপাতত খালি রাখতে পারো।



# 5️⃣ calculator.py Module তৈরি করা
# utilities/calculator.py File-এর মধ্যে লিখো:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# এখানে চারটি Function তৈরি করা হয়েছে:

# add()
# subtract()
# multiply()
# divide()



# 6️⃣ Package থেকে Function Import করা
# এখন main.py-তে লিখো:

# from utilities.calculator import add, subtract, multiply, divide
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# এখানে:
# from utilities.calculator import add
# এর অর্থ:
# utilities  → Package
# calculator → Module
# add        → Function



# 7️⃣ একই main.py-তে দুইটি Module ব্যবহার করা
# এখন main.py-তে Student এবং Calculator—দুটিই ব্যবহার করো:

# import student
# from utilities.calculator import add, subtract, multiply, divide
# print("----- Student Information -----")
# student.introduce()
# print("Adult:", student.is_adult())
# print("\n----- Calculator -----")
# print("Addition:", add(20, 10))
# print("Subtraction:", subtract(20, 10))
# print("Multiplication:", multiply(20, 10))
# print("Division:", divide(20, 10))



# 8️⃣ Module-এর Alias ব্যবহার করা
# চাইলে Package-এর Module-কে Alias দিতে পারো:
# import utilities.calculator as calc
# print(calc.add(10, 5))
# print(calc.multiply(10, 5))

# এখানে
# utilities.calculator → calc
# তাই লিখতে হচ্ছে: calc.add()



# 9️⃣ main.py-তে Menu তৈরি করা
# এখন আমরা Project-টিকে আরও Practical করব।
# import student
# from utilities.calculator import add, subtract, multiply, divide
# print("===== Student Management System =====")
# student.introduce()
# print("\n===== Calculator Menu =====")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# choice = int(input("Enter your choice: "))
# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))

# if choice == 1:
#     print("Result:", add(number1, number2))

# elif choice == 2:
#     print("Result:", subtract(number1, number2))

# elif choice == 3:
#     print("Result:", multiply(number1, number2))

# elif choice == 4:
#     print("Result:", divide(number1, number2))

# else:
#     print("Invalid choice")



# 🔟 if __name__ == "__main__" ব্যবহার
# student.py-তে চাইলে নিচের অংশ যোগ করতে পারো:
name = "Raihan"
age = 23
department = "CSE"

def introduce():
    print("My name is", name)
    print("Age:", age)
    print("Department:", department)

def is_adult():
    return age >= 18

if __name__ == "__main__":
    introduce()
    print("Adult:", is_adult())

# এখন:
# python student.py
# চালালে Output হবে:
# My name is Raihan
# Age: 23
# Department: CSE
# Adult: True

# কিন্তু main.py থেকে:
# import student
# করলে if __name__ == "__main__":-এর ভিতরের Code সরাসরি Run হবে না।

# 🧠 পুরো Project কীভাবে কাজ করছে?
# main.py
#    │
#    ├── student.py
#    │      ├── name
#    │      ├── age
#    │      ├── introduce()
#    │      └── is_adult()
#    │
#    └── utilities
#           └── calculator.py
#                  ├── add()
#                  ├── subtract()
#                  ├── multiply()
#                  └── divide()