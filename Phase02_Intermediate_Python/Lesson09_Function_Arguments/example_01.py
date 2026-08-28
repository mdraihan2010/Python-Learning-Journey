# Positional Argument : যখন Function Call করার সময় Argument-এর Position বা Order অনুযায়ী Parameter-এ Value যায়,তখন তাকে Positional Argument বলে।
# First Argument প্রথম Parameter-এ যায়, Second Argument দ্বিতীয় Parameter-এ যায়, Third Argument তৃতীয় Parameter-এ যায়।


def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


student_info("Raihan", 23, "CSE")