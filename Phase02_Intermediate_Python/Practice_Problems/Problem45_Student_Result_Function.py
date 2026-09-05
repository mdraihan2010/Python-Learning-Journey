# student-এর নাম ও নম্বর নিয়ে result তৈরি করতে হবে।

def calculate_result(name, marks):
    if marks >= 80:
        grade = "A+"
    elif marks >= 70:
        grade = "A"
    elif marks >= 60:
        grade = "A-"
    elif marks >= 50:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "F"

    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


student_name = input("Enter student name: ")
student_marks = float(input("Enter student marks: "))

calculate_result(student_name, student_marks)