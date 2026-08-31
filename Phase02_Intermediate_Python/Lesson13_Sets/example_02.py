# এখন আমরা Python-এ বিভিন্নভাবে Set তৈরি করা শিখব। 🚀

# 1️⃣ সাধারণভাবে Set তৈরি করা : Set তৈরি করতে Curly Braces {} ব্যবহার করা হয়।
numbers = {10, 20, 30, 40, 50}
print(numbers)



# 2️⃣ String দিয়ে Set তৈরি করা
fruits = {"Apple", "Banana", "Mango"}
print(fruits)



# 3️⃣ Different Data Types দিয়ে Set : একটি Set-এর মধ্যে বিভিন্ন ধরনের Data রাখা যায়।
data = {"Raihan", 23, 3.75, True}
print(data)



# 4️⃣ Duplicate Value সহ Set : Set Duplicate Value Automatically Remove করে।
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)



# 5️⃣ Empty Set তৈরি করা ⚠️ : Empty Set তৈরি করতে set() ব্যবহার করতে হবে।
numbers = set()
print(numbers)
print(type(numbers))



# 6️⃣ List থেকে Set তৈরি করা : set() Function ব্যবহার করে একটি List-কে Set-এ Convert করা যায়
numbers = [10, 20, 10, 30, 20]
new_set = set(numbers)
print(new_set)


# 7️⃣ Tuple থেকে Set তৈরি করা
numbers = (10, 20, 10, 30, 20)
new_set = set(numbers)
print(new_set)


# 8️⃣ String থেকে Set তৈরি করা : String-এর প্রতিটি Character নিয়ে Set তৈরি করা যায়।
letters = set("Python")
print(letters)
letters = set("Programming")
print(letters)

# Duplicate Character Automatically Remove হয়ে যাবে।