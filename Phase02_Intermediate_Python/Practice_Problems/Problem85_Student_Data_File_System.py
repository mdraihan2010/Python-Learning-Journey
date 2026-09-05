# file ব্যবহার করে student data সংরক্ষণ ও প্রদর্শন করো।

name = input("Enter student name: ")
age = input("Enter student age: ")
department = input("Enter department: ")
cgpa = input("Enter CGPA: ")

file = open("student_data.txt", "w")

file.write(f"Name: {name}\n")
file.write(f"Age: {age}\n")
file.write(f"Department: {department}\n")
file.write(f"CGPA: {cgpa}\n")

file.close()

file = open("student_data.txt", "r")

student_data = file.read()

file.close()

print("\nStudent Information:")
print(student_data)