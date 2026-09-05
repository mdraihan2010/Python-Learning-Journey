# # এখন আমরা Python-এ Exception Handling শিখব। 🛡️🚀
# Program Run করার সময় কোনো ভুল হলে অনেক সময় Program হঠাৎ বন্ধ হয়ে যায়।
# যেমন:
number = int(input("Enter a number: "))
print(number)

# যদি Input দিই: abc
# তাহলে Error হবে: ValueError
# কারণ "abc"-কে Integer-এ Convert করা যায় না।
# Exception Handling ব্যবহার করে আমরা এই ধরনের Error সুন্দরভাবে Handle করতে পারি।



# 1️⃣ Exception কী? : Program Run করার সময় যে Error তৈরি হয়, তাকে Exception বলা হয়।
# উদাহরণ:
print(10 / 0)

# Output: ZeroDivisionError: division by zero
# কারণ কোনো Number-কে Zero দিয়ে ভাগ করা যায় না।



# 2️⃣ try এবং except : Exception Handle করার জন্য try এবং except ব্যবহার করা হয়।

try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Invalid input")

# Input: abc
# Output: Invalid input
# এখানে:
# try:
# এর ভিতরে যে Code-এ Error হতে পারে, সেটি রাখা হয়।
# আর:
# except:
# Error হলে এই অংশ Execute হয়।



# 3️⃣ নির্দিষ্ট Exception Handle করা : সব ধরনের Error-এর জন্য শুধু except ব্যবহার না করে নির্দিষ্ট Error Handle করা ভালো।

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")

# Input: abc
# Output: Please enter a valid number.



# 4️⃣ ZeroDivisionError
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print("Result:", result)

except ZeroDivisionError:
    print("A number cannot be divided by zero.")

except ValueError:
    print("Please enter valid numbers.")

# Input:
# Enter first number: 10
# Enter second number: 0
# Output:
# A number cannot be divided by zero.



# 5️⃣ একাধিক except : একটি Program-এ একাধিক ধরনের Exception Handle করা যায়।
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# এখানে:
# ValueError        → ভুল ধরনের Input
# ZeroDivisionError → Zero দিয়ে ভাগ করার চেষ্টা



# 6️⃣ else : try Block-এ কোনো Error না হলে else Block Execute হয়।
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)

# সঠিক Input: 25
# Output: You entered: 25
# ভুল Input: abc
# Output: Invalid number.
# 🧠 মনে রাখবে:
# try    → Error হতে পারে এমন Code
# except → Error হলে
# else   → Error না হলে



# 7️⃣ finally : Error হোক বা না হোক, finally Block সবসময় Execute হয়।
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")

# সঠিক Input: 10
# Output: 10
# Program finished.
# ভুল Input: abc
# Output:
# Invalid input.
# Program finished.



# 8️⃣ try-except-else-finally
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Calculation completed.")

# এখানে চারটি অংশ আছে:
# try     → মূল Code
# except  → Error Handle
# else    → Error না হলে
# finally → সবসময় Execute



# 9️⃣ Error Message দেখা : Exception-এর Error Message Variable-এ রাখা যায়।
try:
    number = int("abc")

except ValueError as error:
    print("Error:", error)

# Output: Error: invalid literal for int() with base 10: 'abc'
# এখানে: as error
# এর মাধ্যমে Error-এর বিস্তারিত Message পাওয়া যায়।



# 🔟 Exception ব্যবহার করা : সব ধরনের সাধারণ Exception Handle করতে:
try:
    result = 10 / 0

except Exception as error:
    print("Something went wrong:", error)

# Output: Something went wrong: division by zero
# তবে সম্ভব হলে নির্দিষ্ট Exception ব্যবহার করা ভালো।



# 1️⃣1️⃣ raise দিয়ে নিজে Exception তৈরি করা :কখনো কখনো আমরা নিজেরাই Error তৈরি করতে চাই।
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Age:", age)

# Input: -5
# Output:
# ValueError: Age cannot be negative.
# এখানে: raise ব্যবহার করে নিজে Exception তৈরি করা হয়েছে।



# 1️⃣2️⃣ Function-এর মধ্যে Exception Handling
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."
print(divide(10, 2))
print(divide(10, 0))

# Output:
# 5.0
# Cannot divide by zero.



# 1️⃣3️⃣ Input Validation : User যতক্ষণ সঠিক Input না দেবে, ততক্ষণ Input নেওয়া যায়।
while True:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        break

    except ValueError:
        print("Invalid input. Try again.")

# Input: abc
# Output: Invalid input. Try again.
# আবার Input: 50
# Output: You entered: 50
# এখানে:break সঠিক Input পেলে Loop বন্ধ করে দেয়।



# 1️⃣4️⃣ File Handling-এ Exception Handling
# আগের Lesson-এর File Project-এ এটি ব্যবহার করেছিলাম।

try:
    with open("student.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")

# যদি student.txt না থাকে, তাহলে Program বন্ধ না হয়ে দেখাবে:
# File not found.



# 1️⃣5️⃣ Practical Calculator Program
while True:
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Result:", number1 + number2)

        elif choice == 2:
            print("Result:", number1 - number2)

        elif choice == 3:
            print("Result:", number1 * number2)

        elif choice == 4:
            print("Result:", number1 / number2)

        else:
            print("Invalid choice.")

        break

    except ValueError:
        print("Please enter valid numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


# 🧠 Common Python Exceptions
# ValueError          → ভুল Value
# TypeError           → ভুল Data Type
# ZeroDivisionError   → Zero দিয়ে ভাগ
# FileNotFoundError   → File পাওয়া যায়নি
# IndexError          → ভুল List Index
# KeyError            → Dictionary-তে Key নেই
# NameError           → Variable পাওয়া যায়নি



# 🧠 Normal Code বনাম Exception Handling


# Normal Code:
number = int(input("Enter a number: "))
print(number)

# ভুল Input দিলে Program বন্ধ হয়ে যেতে পারে।


# Exception Handling:
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")

# ভুল Input দিলেও Program সুন্দরভাবে Error Handle করবে।