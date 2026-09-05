# recursion ব্যবহার করে ১ থেকে N পর্যন্ত যোগফল বের করতে হবে।

def calculate_sum(number):
    if number == 0:
        return 0

    return number + calculate_sum(number - 1)


n = int(input("Enter the value of N: "))

result = calculate_sum(n)

print("Sum:", result)