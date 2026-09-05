# একটি range-এর মধ্যে নির্দিষ্ট number আছে কি না খুঁজে বের করতে হবে।

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
search_number = int(input("Enter the number to search: "))

found = False

for number in range(start, end + 1):
    if number == search_number:
        found = True
        break

if found:
    print("Number found in the range.")
else:
    print("Number not found in the range.")