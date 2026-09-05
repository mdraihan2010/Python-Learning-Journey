# একটি menu-driven program তৈরি করতে হবে।


print("===== Menu =====")
print("1. Say Hello")
print("2. Show Your Name")
print("3. Show Your Age")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Hello! Welcome to Python.")

    case 2:
        name = input("Enter your name: ")
        print("Your name is:", name)

    case 3:
        age = int(input("Enter your age: "))
        print("Your age is:", age)

    case 4:
        print("Program exited.")

    case _:
        print("Invalid choice")