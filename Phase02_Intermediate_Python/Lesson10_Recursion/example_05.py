# Base Case কোথায় থাকে? ->সাধারণত Recursive Function-এর শুরুতেই Base Case লেখা হয়।

# Syntex

# def function_name(value):

#     if stopping_condition:
#         return something

#     function_name(updated_value)

# সবচেয়ে গুরুত্বপূর্ণ Rule ⚠️ : একটি ভালো Recursive Function-এ তিনটি বিষয় থাকতে হবে:
# 1. Base Case থাকতে হবে
# 2. Function নিজেকে Call করবে
# 3. প্রতিবার Recursive Call Base Case-এর দিকে এগোতে হবে।

# Example:

def countdown(number):

    if number == 0:
        return

    countdown(number - 1)

# এখানে:
# Base Case:
# number == 0

# Recursive Call:
# countdown(number - 1)

# Base Case-এর দিকে যাচ্ছে: 5 → 4 → 3 → 2 → 1 → 0


# একটি ভুল Example ❌
def test(number):

    if number == 0:
        return

    test(number + 1)

# যদি: test(5) Call করি, তাহলে: 5 → 6 → 7 → 8 → 9 → ...
# number কখনো 0-এর দিকে যাচ্ছে না। তাই Base Case থাকলেও Function সেখানে পৌঁছাবে না। 😅