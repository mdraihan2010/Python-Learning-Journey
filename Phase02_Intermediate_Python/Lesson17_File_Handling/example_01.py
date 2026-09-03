# এখন আমরা Python-এ File Handling শিখব। 📂🚀
# File Handling ব্যবহার করে আমরা Python দিয়ে File:
# তৈরি করতে পারি
# Open করতে পারি
# Read করতে পারি
# Write করতে পারি
# নতুন Content যোগ করতে পারি
# Delete করতে পারি


# 1️⃣ File Open করা
# File Open করার জন্য open() Function ব্যবহার করা হয়।

file = open("data.txt", "r")
file.close()
# এখানে:
# data.txt → File-এর নাম
# r         → Read Mode
# File ব্যবহার শেষে Close করতে হয়।


# 2️⃣ File Read করা
# প্রথমে একই Folder-এ data.txt নামে একটি File তৈরি করো।
# data.txt:
# Hello Python
# I am learning File Handling.
# এখন main.py-তে লিখো:

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()



# 3️⃣ with open() ব্যবহার করা
# File Handling-এর জন্য সবচেয়ে ভালো পদ্ধতি হলো with open() ব্যবহার করা।

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# এখানে File আলাদাভাবে close() করতে হয় না।
# Python নিজে থেকেই File Close করে দেয়।



# 4️⃣ File-এর প্রতিটি Line Read করা
with open("data.txt", "r") as file:
    for line in file:
        print(line)

# Extra Blank Line এড়াতে:

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5️⃣ readline()
# একটি করে Line Read করতে readline() ব্যবহার করা হয়।

with open("data.txt", "r") as file:
    print(file.readline())
    print(file.readline())



# 6️⃣ readlines()
# সব Line একটি List হিসেবে পেতে readlines() ব্যবহার করা হয়।
with open("data.txt", "r") as file:
    lines = file.readlines()
print(lines)



# 7️⃣ File Write করা
# File-এ নতুন Content লেখার জন্য w Mode ব্যবহার করা হয়।

with open("data.txt", "w") as file:
    file.write("Python is easy to learn.")



# 8️⃣ একাধিক Line Write করা
with open("data.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")



# 9️⃣ File-এ Content যোগ করা : পুরোনো Content না মুছে নতুন Content যোগ করতে a Mode ব্যবহার করা হয়।

with open("data.txt", "a") as file:
    file.write("\nLine 4")

# 🧠 মনে রাখবে:
# w → Write / Overwrite
# a → Append / নতুন Content যোগ
# r → Read



# 🔟 File-এর Mode
# r  → Read করার জন্য
# w  → Write করার জন্য
# a  → Append করার জন্য
# x  → নতুন File তৈরি করার জন্য
# x Mode
with open("new_file.txt", "x") as file:
    file.write("This is a new file.")

# File আগে থেকে থাকলে Error হবে।



# 1️⃣1️⃣ File আছে কি না Check করা
# os Module ব্যবহার করে File আছে কি না Check করা যায়।

import os
if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")



# 1️⃣2️⃣ File Delete করা

import os
if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File deleted")
else:
    print("File does not exist")



# 1️⃣3️⃣ File-এর Content Count করা
with open("data.txt", "r") as file:
    content = file.read()
print("Characters:", len(content))



# 1️⃣4️⃣ File-এর Word Count করা
with open("data.txt", "r") as file:
    content = file.read()
words = content.split()
print("Words:", len(words))



# 1️⃣5️⃣ File-এর Line Count করা
with open("data.txt", "r") as file:
    lines = file.readlines()
print("Lines:", len(lines))



# 1️⃣6️⃣ Student Information File-এ Save করা
name = input("Enter your name: ")
age = input("Enter your age: ")
department = input("Enter your department: ")
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Department: " + department + "\n")
print("Student information saved successfully.")



# 1️⃣7️⃣ File থেকে Student Information Read করা
with open("student.txt", "r") as file:
    content = file.read()
print(content)

# 🧠 File Handling-এর সবচেয়ে গুরুত্বপূর্ণ Pattern
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Write:

with open("data.txt", "w") as file:
    file.write("Hello Python")

# Append:

with open("data.txt", "a") as file:
    file.write("\nNew Line")