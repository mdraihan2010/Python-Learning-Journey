# user zero ইনপুট না দেওয়া পর্যন্ত সংখ্যা নিতে হবে এবং যোগফল বের করতে হবে।

total = 0

while True:
    number = float(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Sum:", total)