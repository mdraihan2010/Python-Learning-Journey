# একটি range-এর মধ্যে প্রথম divisible number খুঁজে বের করতে হবে।

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
divisor = int(input("Enter divisor: "))

found = False

for number in range(start, end + 1):
    if number % divisor == 0:
        print("First divisible number:", number)
        found = True
        break

if not found:
    print("No divisible number found.")