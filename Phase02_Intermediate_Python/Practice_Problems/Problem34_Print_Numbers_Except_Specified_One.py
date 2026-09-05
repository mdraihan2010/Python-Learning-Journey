# একটি নির্দিষ্ট সংখ্যা বাদ দিয়ে অন্য সংখ্যা print করতে হবে।

n = int(input("Enter the value of N: "))
excluded_number = int(input("Enter the number to exclude: "))

for number in range(1, n + 1):
    if number == excluded_number:
        continue

    print(number)