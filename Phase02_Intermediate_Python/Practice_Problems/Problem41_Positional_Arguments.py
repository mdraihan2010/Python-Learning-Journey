# positional arguments ব্যবহার করে একটি function তৈরি করতে হবে।

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))

introduce(student_name, student_age)