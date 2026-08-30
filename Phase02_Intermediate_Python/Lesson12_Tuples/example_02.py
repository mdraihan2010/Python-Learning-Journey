# এখন আমরা শিখব Python-এ বিভিন্নভাবে Tuple তৈরি করা। 🚀

# 1️⃣ সাধারণভাবে Tuple তৈরি করা : Tuple তৈরি করতে সাধারণত () ব্যবহার করা হয়।
fruits = ("Apple", "Banana", "Mango")
print(fruits)


# 2️⃣ Number Tuple
numbers = (10, 20, 30, 40, 50)
print(numbers)


# 3️⃣ Different Data Types দিয়ে Tuple : একটি Tuple-এর মধ্যে বিভিন্ন ধরনের Data রাখা যায়।
student = ("Raihan", 23, 3.75, True)
print(student)


# 4️⃣ Empty Tuple : খালি Tuple তৈরি করতে:
numbers = ()
print(numbers)


# 5️⃣ একটি মাত্র Element-এর Tuple ⚠️ : একটি Single Element Tuple তৈরি করতে Element-এর পরে Comma , দিতে হবে।
number = (10,)
print(type(number))


# 6️⃣ Duplicate Value সহ Tuple : Tuple একই Value একাধিকবার Store করতে পারে।
numbers = (10, 20, 10, 30, 20)
print(numbers)


# 7️⃣ Nested Tuple : একটি Tuple-এর ভিতরে আরেকটি Tuple থাকতে পারে।
numbers = (1, 2, (3, 4), 5)
print(numbers)


# 8️⃣ tuple() Function ব্যবহার করে Tuple তৈরি
numbers = tuple([10, 20, 30])
print(numbers)