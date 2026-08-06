# Write a Program to input a student's name, roll, age, department, and CGPA. Print all the information, the data type of each variable, and check whether the CGPA is greater than or equal to 3.50.

name = input("Enter student's name: ")
roll = int(input("Enter student's roll number: "))
age = int(input("Enter student's age: "))
department = input("Enter student's department: ")
CGPA = float(input("Enter student's CGPA: "))

print("\nStudent Information:")
print("Name:", name)
print("Roll Number:", roll)
print("Age:", age)
print("Department:", department)
print("CGPA:", CGPA)

print("\nData Types:")
print("Name:", type(name))
print("Roll Number:", type(roll))
print("Age:", type(age))
print("Department:", type(department))
print("CGPA:", type(CGPA))

print("\nCGPA Check:")
print("Is CGPA greater than or equal to 3.50?", CGPA >= 3.50)