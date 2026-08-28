# Function-এর Return Value ব্যবহার করার বিভিন্ন উপায়

# 1. সরাসরি Print করা
def square1(number):
    return number ** 2

print(square1(5))


# 2. Variable-এ রাখা
def square2(number):
    return number ** 2

result = square2(5)

print(result)


# 3. অন্য Calculation-এ ব্যবহার করা
def square3(number):
    return number ** 2

result = square3(5) + 10

print(result)

