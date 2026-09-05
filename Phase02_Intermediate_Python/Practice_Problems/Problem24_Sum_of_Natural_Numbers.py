# ১ থেকে N পর্যন্ত সংখ্যার যোগফল বের করতে হবে।


n = int(input("Enter the value of N: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum:", total)