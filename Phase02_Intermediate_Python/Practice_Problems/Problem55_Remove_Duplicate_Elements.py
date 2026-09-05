# list থেকে duplicate element সরিয়ে ফেলতে হবে।

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List without duplicates:", unique_numbers)