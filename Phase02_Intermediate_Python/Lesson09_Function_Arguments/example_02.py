# Keyword Argument : যখন Function Call করার সময় আমরা সরাসরি Parameter-এর নাম উল্লেখ করে Value দিই, তখন তাকে Keyword Argument বলে।
# Parameter-এর নাম = Value লিখে Function Call করাকে Keyword Argument বলে।


def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


student_info(name="Raihan", age=23, department="CSE")