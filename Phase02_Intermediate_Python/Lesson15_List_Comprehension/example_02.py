# এখন আমরা List Comprehension-এর মধ্যে Condition (if) ব্যবহার করা শিখব। 🚀
# Condition যোগ করলে: [expression for item in iterable if condition]
# এখানে condition True হলে শুধু সেই Element-টি নতুন List-এ যাবে।



# 1️⃣ শুধু Even Numbers
numbers = range(1, 11)
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# এখানে: number % 2 == 0
# Condition True হলেই Number List-এ যোগ হচ্ছে।



# 2️⃣ শুধু Odd Numbers
numbers = range(1, 11)
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)



# 3️⃣ 50-এর বেশি Number
numbers = [20, 55, 70, 35, 90, 45]
result = [number for number in numbers if number > 50]
print(result)



# 4️⃣ Positive Numbers
numbers = [-5, 10, -2, 20, 0, 15]
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)



# 5️⃣ String থেকে Vowel বের করা
word = "programming"
vowels = [letter for letter in word if letter in "aeiou"]
print(vowels)



# 6️⃣ Condition + Expression : শুধু Even Number নেওয়ার পাশাপাশি তাদের Square করতে পারি।
numbers = range(1, 11)
squares = [number ** 2 for number in numbers if number % 2 == 0]
print(squares)

# এখানে প্রথমে Even Number নেওয়া হচ্ছে, তারপর তার Square তৈরি হচ্ছে।



# 🧠 Normal Loop বনাম List Comprehension
# Normal:
numbers = []
for number in range(1, 11):

    if number % 2 == 0:
        numbers.append(number)
print(numbers)


# List Comprehension:
numbers = [number for number in range(1, 11) if number % 2 == 0]
print(numbers)
