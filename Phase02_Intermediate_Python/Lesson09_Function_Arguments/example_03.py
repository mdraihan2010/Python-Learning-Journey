# Keyword Argument-এর সবচেয়ে বড় সুবিধা 🧠 : এখানে Order পরিবর্তন করলেও সমস্যা হয় না।


def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

student_info(
    department="CSE",
    name="Raihan",
    age=23
)