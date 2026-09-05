# নম্বর ইনপুট নিয়ে grade নির্ণয় করতে হবে।


marks = float(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: A-")
elif marks >= 50:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks")