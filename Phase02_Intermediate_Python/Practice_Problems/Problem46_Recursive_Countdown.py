# recursion ব্যবহার করে countdown তৈরি করতে হবে।

def countdown(number):
    if number < 1:
        return

    print(number)
    countdown(number - 1)


n = int(input("Enter the starting number: "))

countdown(n)