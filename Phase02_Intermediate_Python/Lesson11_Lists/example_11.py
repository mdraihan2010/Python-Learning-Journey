# এখন আমরা শিখব List-এর প্রতিটি Element কীভাবে Loop ব্যবহার করে Access করা যায়। 🚀


# 1️⃣ for Loop ব্যবহার করে

fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)


# 2️⃣ Number List-এর মাধ্যমে Loop

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print(number)


# 3️⃣ Loop ব্যবহার করে Calculation : ধরো List-এর সব Number-এর Sum বের করতে চাই।

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number

print("Sum =", total)



# 4️⃣ Index ব্যবহার করে Loop : আমরা range() এবং len() ব্যবহার করেও List Loop করতে পারি।

fruits = ["Apple", "Banana", "Mango"]
for index in range(len(fruits)):
    print(index, fruits[index])



# 5️⃣ enumerate() ব্যবহার করে : একসাথে Index এবং Value পাওয়ার জন্য enumerate() ব্যবহার করা যায়।

fruits = ["Apple", "Banana", "Mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)



# 6️⃣ নির্দিষ্ট Condition অনুযায়ী Print

numbers = [10, 15, 20, 25, 30]
for number in numbers:
    if number % 2 == 0:
        print(number)



# 7️⃣ List-এর সব Element Square করা

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number ** 2)




