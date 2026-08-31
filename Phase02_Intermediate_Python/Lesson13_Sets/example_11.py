# এখন আমরা শিখব Set-এর প্রতিটি Element কীভাবে Loop ব্যবহার করে Access করা যায়। 🚀


# 1️⃣ Basic for Loop
fruits = {"Apple", "Banana", "Mango"}
for fruit in fruits:
    print(fruit)



# 2️⃣ Number Set Loop করা
numbers = {10, 20, 30, 40, 50}
for number in numbers:
    print(number)



# 3️⃣ Loop ব্যবহার করে Sum বের করা
numbers = {10, 20, 30, 40, 50}
total = 0
for number in numbers:
    total = total + number
print("Sum =", total)



# 4️⃣ শুধু Even Number Print করা
numbers = {10, 15, 20, 25, 30}
for number in numbers:
    if number % 2 == 0:
        print(number)



# 5️⃣ শুধু Odd Number Print করা
numbers = {10, 15, 20, 25, 30}
for number in numbers:
    if number % 2 != 0:
        print(number)



# 6️⃣ প্রতিটি Number-এর Square Print করা
numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print(number ** 2)



# 7️⃣ break ব্যবহার করে Loop বন্ধ করা
numbers = {10, 20, 30, 40, 50}
for number in numbers:
    if number == 30:
        break
    print(number)



# 8️⃣ continue ব্যবহার করা
numbers = {10, 15, 20, 25, 30}
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)



# 🧠 সবচেয়ে গুরুত্বপূর্ণ Syntax
# for variable in set_name:
#     print(variable)

# Example:

for fruit in fruits:
    print(fruit)