# ১ থেকে ১০০ পর্যন্ত ৩-এর গুণিতক বাদ দিয়ে print করতে হবে।

for number in range(1, 101):
    if number % 3 == 0:
        continue

    print(number)