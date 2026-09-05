# recursion ব্যবহার করে Fibonacci series তৈরি করতে হবে।

def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


n = int(input("Enter the number of terms: "))

for number in range(n):
    print(fibonacci(number), end=" ")