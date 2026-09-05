# keyword arguments ব্যবহার করে student information print করতে হবে।

def show_student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_department = input("Enter department: ")

show_student_info(
    name=student_name,
    age=student_age,
    department=student_department
)