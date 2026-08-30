# এখন আমরা শিখব Tuple-এর প্রতিটি Element কীভাবে Loop ব্যবহার করে Access করা যায়। 🚀


# 1️⃣ for Loop ব্যবহার করে : Tuple-এর প্রতিটি Element Print করতে:
fruits = ("Apple", "Banana", "Mango", "Orange")
for fruit in fruits:
    print(fruit)



# 2️⃣ Number Tuple-এর মাধ্যমে Loop
numbers = (10, 20, 30, 40, 50)
for number in numbers:
    print(number)



# 3️⃣ Loop ব্যবহার করে Sum বের করা
numbers = (10, 20, 30, 40, 50)
total = 0
for number in numbers:
    total = total + number
print("Sum =", total)



# 4️⃣ Index ব্যবহার করে Loop : range() এবং len() ব্যবহার করে Tuple Loop করা যায়।

fruits = ("Apple", "Banana", "Mango")
for index in range(len(fruits)):
    print(index, fruits[index])



# 5️⃣ enumerate() ব্যবহার করে : একসাথে Index এবং Value পাওয়ার জন্য:

fruits = ("Apple", "Banana", "Mango")
for index, fruit in enumerate(fruits):
    print(index, fruit)



# 6️⃣ শুধু Even Number Print করা
numbers = (10, 15, 20, 25, 30)
for number in numbers:
    if number % 2 == 0:
        print(number)



# 7️⃣ Tuple-এর প্রতিটি Number-এর Square Print করা
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number ** 2)
