# যোগ, বিয়োগ, গুণ ও ভাগের জন্য একটি custom math module তৈরি করো।

# math_module.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b