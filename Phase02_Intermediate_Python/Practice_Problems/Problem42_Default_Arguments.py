# default argument ব্যবহার করে greeting function তৈরি করতে হবে।

def greet(name="Guest"):
    print("Hello,", name)


user_name = input("Enter your name: ")

if user_name == "":
    greet()
else:
    greet(user_name)