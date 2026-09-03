# এখন আমরা Python-এর Modules and Packages শিখব। 🚀
# বড় Project-এ সব Code একসাথে একটি File-এ রাখলে Code অনেক বড় ও জটিল হয়ে যায়। তাই আমরা Code-কে আলাদা আলাদা File এবং Folder-এ ভাগ করে রাখি।
# Module → একটি Python File
# Package → একাধিক Related Module-এর Folder
# Import → অন্য File-এর Code ব্যবহার করা



# 1️⃣ Module কী? একটি Python .py File-কে Module বলা হয়।

# ধরো, আমরা একটি File তৈরি করলাম: 
from py_compile import main
main("calculator.py")
# এই File-এর মধ্যে Function, Variable ইত্যাদি রাখা যায়।

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# এখানে calculator.py হলো একটি Module।



# 2️⃣ Module Import করা : এখন একই Folder-এ আরেকটি File তৈরি করি:
main.py
# main.py থেকে calculator.py ব্যবহার করতে:

# import calculator
# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))

# এখানে:
# import calculator মানে calculator.py Module-টি Import করা হয়েছে।
# আর: calculator.add(10, 5) মানে calculator Module-এর add() Function ব্যবহার করা হয়েছে।



# 3️⃣ নির্দিষ্ট Function Import করা : পুরো Module Import না করে নির্দিষ্ট Function Import করা যায়।
# from calculator import add
print(add(10, 5))

# এখানে add() Function সরাসরি ব্যবহার করা হয়েছে।
# from calculator import add
# মানে calculator Module থেকে শুধু add() Function Import করা হয়েছে।



# 4️⃣ একাধিক Function Import করা
# from calculator import add, subtract
print(add(20, 10))
print(subtract(20, 10))



# 5️⃣ Module-এর Alias তৈরি করা : Module-এর নাম ছোট করে ব্যবহার করতে Alias দেওয়া যায়।
# import calculator as calc
# print(calc.add(20, 10))
# print(calc.subtract(20, 10))



# 6️⃣ Function-এর Alias তৈরি করা
# from calculator import add as addition
# print(addition(10, 20))



# 7️⃣ Module-এর মধ্যে Variable রাখা : Module-এর মধ্যে Function ছাড়াও Variable রাখা যায়।
# student.py:
# name = "Raihan"
# age = 23
# department = "CSE"
# main.py:
# import student
# print(student.name)
# print(student.age)
# print(student.department)


# 8️⃣ Module-এর মধ্যে Function এবং Variable
# student.py
# name = "Raihan"
# age = 23
# def introduce():
#     print("My name is", name)
# main.py:
# import student
# print(student.name)
# print(student.age)
# student.introduce()



# 9️⃣ Python-এর Built-in Module : Python-এর সাথে অনেক Built-in Module থাকে।
# কিছু Built-in Module:
# math
# random
# datetime
# os
# statistics



# 🔟 math Module : গাণিতিক কাজের জন্য math Module ব্যবহার করা হয়।
import math
print(math.sqrt(25))



# 1️⃣1️⃣ math Module-এর আরও কিছু Function
import math
print(math.sqrt(16))
print(math.ceil(4.2))
print(math.floor(4.8))



# 1️⃣2️⃣ math.pi : Circle-এর Area বের করতে math.pi ব্যবহার করা যায়।
import math
radius = 5
area = math.pi * radius ** 2
print(area)



# 1️⃣3️⃣ random Module : Random Number তৈরি করতে random Module ব্যবহার করা হয়।
import random
number = random.randint(1, 10)
print(number)


# 1️⃣4️⃣ random.choice() : একটি List থেকে Random Element বাছাই করতে choice() ব্যবহার করা হয়।
import random
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruit = random.choice(fruits)
print(fruit)



# 1️⃣5️⃣ datetime Module : বর্তমান Date বের করতে datetime Module ব্যবহার করা যায়।
import datetime
today = datetime.date.today()
print(today)



# 1️⃣6️⃣ if __name__ == "__main__" : কোনো File সরাসরি Run করলে এবং অন্য File থেকে Import করলে—দুই অবস্থার আচরণ আলাদা করার জন্য এটি ব্যবহার করা হয়।
# calculator.py:
# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print(add(10, 20))

# এখন calculator.py সরাসরি Run করলে: 30
# কিন্তু অন্য File থেকে: import calculator
# করলে শুধু add() Function Import হবে।
# if __name__ == "__main__":-এর ভিতরের print() অংশটি তখন সরাসরি Execute হবে না।



# 1️⃣7️⃣ Package কী? : Package হলো Related একাধিক Module-এর একটি Folder।
# ধরো আমাদের Folder Structure:
# mypackage/
#     __init__.py
#     calculator.py
#     geometry.py
# এখানে:
# calculator.py → Module
# geometry.py   → Module
# mypackage     → Package
# __init__.py File Package-এর অংশ হিসেবে রাখা হয়।



# 1️⃣8️⃣ Package-এর Module Import করা
# ধরো mypackage/calculator.py:

# def add(a, b):
#     return a + b

# এখন main.py থেকে: from mypackage import calculator
# print(calculator.add(10, 20))



# 1️⃣9️⃣ Package থেকে সরাসরি Function Import করা
# from mypackage.calculator import add
# print(add(10, 20))

# এখানে: mypackage.calculator
# মানে:
# mypackage → Package
# calculator → Module
# আর add হলো সেই Module-এর Function।


# 🧠 Module বনাম Package
# Module → একটি Python File
# Example → calculator.py
# Package → Related Module-এর Folder
# Example → mypackage/

# সহজভাবে: Module হলো একটি File, আর Package হলো একাধিক Related File-এর Folder।



# 2️⃣0️⃣ Realistic Project Structure
# ধরো আমরা একটি Student Management Project তৈরি করছি:
# student_management/
# │
# ├── main.py
# │
# ├── students/
# │   ├── __init__.py
# │   ├── student.py
# │   ├── result.py
# │   └── attendance.py
# │
# └── utilities/
#     ├── __init__.py
#     ├── calculator.py
#     └── validator.py

# এখানে:
# main.py       → Main Program
# students      → Package
# student.py    → Student-related Module
# result.py     → Result-related Module
# attendance.py → Attendance-related Module
# utilities     → Package
# calculator.py → Calculation-related Module
# validator.py  → Validation-related Module



# 🧠 সবচেয়ে গুরুত্বপূর্ণ Import Syntax
# import module
# from module import function
# from module import function1, function2
# import module as alias
# from module import function as alias
# from package import module
# from package.module import function