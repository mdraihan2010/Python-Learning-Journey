# negative number পাওয়া গেলে loop বন্ধ করতে হবে।

while True:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Negative number found. Loop stopped.")
        break

    print("You entered:", number)