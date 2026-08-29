# এখন আমরা শিখব List থেকে কোনো Element কীভাবে Remove বা Delete করতে হয়। 🚀


# 1️⃣ remove() Method : remove() ব্যবহার করে নির্দিষ্ট Value Remove করা হয়।
# Syntax : list_name.remove(value)
# Example:

fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)

# ⚠️ যদি একই Value একাধিকবার থাকে, তাহলে remove() শুধুমাত্র প্রথম পাওয়া Value Remove করবে।

numbers = [10, 20, 10, 30]
numbers.remove(10)
print(numbers)



# 2️⃣ pop() Method : pop() ব্যবহার করে সাধারণত শেষ Element Remove করা হয়।

fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)



# ⚠️ নির্দিষ্ট Index থেকেও Remove করা যায়

fruits = ["Apple", "Banana", "Mango"]
fruits.pop(1)
print(fruits)



# 3️⃣ del Keyword : del ব্যবহার করে Index অনুযায়ী Element Delete করা যায়।

numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)


# ⚠️ Slicing ব্যবহার করেও Delete করা যায়

numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)



# 4️⃣ clear() Method : clear() ব্যবহার করে List-এর সব Element Remove করা যায়।

fruits = ["Apple", "Banana", "Mango"]
fruits.clear()
print(fruits)


# remove() Value দিয়ে Remove করে, 
# pop() Index দিয়ে বা শেষ থেকে Remove করে, 
# del দিয়ে Delete করা যায়,
# clear() পুরো List খালি করে দেয়।