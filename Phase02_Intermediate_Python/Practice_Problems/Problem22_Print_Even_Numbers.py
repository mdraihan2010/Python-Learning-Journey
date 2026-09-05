# ১ থেকে N পর্যন্ত সব জোড় সংখ্যা print করতে হবে।


n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)