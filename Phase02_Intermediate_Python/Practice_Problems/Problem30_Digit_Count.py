# একটি সংখ্যায় কয়টি digit আছে তা বের করতে হবে।

number = int(input("Enter a number: "))

number = abs(number)

if number == 0:
    digit_count = 1
else:
    digit_count = 0

    while number > 0:
        number //= 10
        digit_count += 1

print("Number of digits:", digit_count)