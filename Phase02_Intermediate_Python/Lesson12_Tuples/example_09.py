# এখন আমরা শিখব Tuple থেকে কোনো Element কীভাবে Remove করা যায়। 🚀


# 1️⃣ List-এ Convert করে Element Remove করা : Tuple → List → Remove → আবার Tuple
fruits = ("Apple", "Banana", "Mango")
fruits_list = list(fruits)
fruits_list.remove("Banana")
fruits = tuple(fruits_list)
print(fruits)



# 2️⃣ নির্দিষ্ট Index-এর Element Remove করা : pop() ব্যবহার করে List থেকে নির্দিষ্ট Index-এর Element Remove করা যায়।
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
numbers_list.pop(1)
numbers = tuple(numbers_list)
print(numbers)



# 3️⃣ শেষ Element Remove করা
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
numbers_list.pop()
numbers = tuple(numbers_list)
print(numbers)



# 4️⃣ del ব্যবহার করে Tuple-এর একটি Variable Delete করা : del ব্যবহার করে পুরো Tuple Variable Delete করা যায়।

fruits = ("Apple", "Banana", "Mango")
del fruits
