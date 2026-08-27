# 1 থেকে 10 পর্যন্ত যোগফল

number = int(input("Enter a number: "))
total = 0

for i in range(1, number + 1):
    total = total + i

print("Total =", total)