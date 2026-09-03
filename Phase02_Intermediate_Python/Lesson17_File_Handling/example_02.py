# এখন আমরা File Handling ব্যবহার করে একটি ছোট Student Information Management System তৈরি করব। 🚀
# এই Project-এ আমরা শিখব:
# User Input নেওয়া
# File-এ Data Save করা
# File থেকে Data Read করা
# নতুন Data Append করা
# File-এর Line Count করা
# Menu তৈরি করা



# 1️⃣ Project Structure
# একটি Folder তৈরি করো:
# File_Handling_Project/
# │
# └── main.py

# এখন শুধু main.py File তৈরি করলেই হবে।
# Program Run করলে প্রয়োজন অনুযায়ী student.txt File নিজে তৈরি হবে।



# 2️⃣ Student Information Save করা
# main.py:
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Department: " + department + "\n")
print("Student information saved successfully.")



# 3️⃣ File থেকে Data Read করা
with open("student.txt", "r") as file:
    content = file.read()
print(content)



# 4️⃣ File-এ নতুন Line যোগ করা
with open("student.txt", "a") as file:
    file.write("University: JUST\n")
print("New information added.")



# 5️⃣ File-এর Line Count করা
with open("student.txt", "r") as file:
    lines = file.readlines()
print("Total Lines:", len(lines))



# 6️⃣ সম্পূর্ণ Practical Program
# এখন আমরা সবকিছু একটি Menu-এর মধ্যে রাখব।

def save_student():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    department = input("Enter your department: ")
    with open("student.txt", "w") as file:
        file.write("Name: " + name + "\n")
        file.write("Age: " + age + "\n")
        file.write("Department: " + department + "\n")
    print("Student information saved successfully.")

def read_student():
    try:
        with open("student.txt", "r") as file:
            content = file.read()

        print("\n----- Student Information -----")
        print(content)

    except FileNotFoundError:
        print("Student file not found.")

def append_information():
    information = input("Enter new information: ")

    with open("student.txt", "a") as file:
        file.write(information + "\n")

    print("Information added successfully.")

def count_lines():
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()

        print("Total Lines:", len(lines))

    except FileNotFoundError:
        print("Student file not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Save Student Information")
    print("2. Read Student Information")
    print("3. Add New Information")
    print("4. Count Total Lines")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        save_student()

    elif choice == "2":
        read_student()

    elif choice == "3":
        append_information()

    elif choice == "4":
        count_lines()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")


# 7️⃣ Program-এর Sample Run
# ===== Student Management System =====
# 1. Save Student Information
# 2. Read Student Information
# 3. Add New Information
# 4. Count Total Lines
# 5. Exit

# Enter your choice: 1
# Enter your name: Raihan
# Enter your age: 23
# Enter your department: CSE
# Student information saved successfully.

# আবার Menu আসবে:

# Enter your choice: 2

# ----- Student Information -----
# Name: Raihan
# Age: 23
# Department: CSE

# নতুন Information যোগ করতে:

# Enter your choice: 3
# Enter new information: University: JUST
# Information added successfully.


# 🧠 try-except কেন ব্যবহার করেছি?
# যদি student.txt File না থাকে, তাহলে:
# open("student.txt", "r")
# ব্যবহার করলে FileNotFoundError হতে পারে।
# তাই:
# try:
#     # File Read করার Code
# except FileNotFoundError:
#     print("Student file not found.")

# ব্যবহার করেছি।
# এতে Program হঠাৎ বন্ধ না হয়ে সুন্দরভাবে Error Message দেখাবে।