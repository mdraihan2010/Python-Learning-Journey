# এখন আমরা List Comprehension-এর মধ্যে একাধিক Condition ব্যবহার করা শিখব। 🚀



# 1️⃣ Even Number এবং 10-এর বেশি
numbers = range(1, 21)
result = [number for number in numbers if number % 2 == 0 and number > 10]
print(result)

# Output: [12, 14, 16, 18, 20]
# এখানে দুটি Condition আছে:
# 1. number % 2 == 0 → Number অবশ্যই Even হতে হবে।
# 2. number > 10 → Number 10-এর বেশি হতে হবে।
# দুটি Condition-ই True হলেই Number List-এ যাবে।



# 2️⃣ 5-এর বেশি এবং 15-এর কম
numbers = range(1, 21)
result = [number for number in numbers if number > 5 and number < 15]
print(result)


# 3️⃣ Even Number অথবা 5 দিয়ে Divisible
numbers = range(1, 21)
result = [number for number in numbers if number % 2 == 0 or number % 5 == 0]
print(result)

# এখানে:
# Even হলে → List-এ যাবে অথবা 5 দিয়ে Divisible হলে → List-এ যাবে
# যেকোনো একটি Condition True হলেই হবে।



# 4️⃣ Positive এবং Even Number
numbers = [-10, -5, 2, 4, -8, 10, 15, -20]
result = [number for number in numbers if number > 0 and number % 2 == 0]
print(result)

# এখানে Number-কে:
# Positive হতে হবে এবং Even হতে হবে।



# 5️⃣ Positive অথবা Zero
numbers = [-5, 10, -2, 0, 15, -8]
result = [number for number in numbers if number > 0 or number == 0]
print(result)



# 6️⃣ Multiple Conditions + Expression
numbers = range(1, 21)
result = [number ** 2 for number in numbers if number % 2 == 0 and number > 10]
print(result)

# Output: [144, 196, 256, 324, 400]
# এখানে প্রথমে:
# Even Number এবং 10-এর বেশি Number নেওয়া হচ্ছে।
# তারপর সেই Number-এর Square তৈরি হচ্ছে।



# 7️⃣ String-এর ক্ষেত্রে Multiple Conditions
words = ["apple", "banana", "cat", "elephant", "dog", "orange"]
result = [word for word in words if len(word) > 5 and word.startswith("a")]
print(result)

# Output: ['apple']
# এখানে দুটি Condition:
# 1. Word-এর Length 5-এর বেশি
# 2. Word "a" দিয়ে শুরু
# দুটি Condition-ই True হতে হবে।



# 8️⃣ Vowel এবং Length Condition
words = ["apple", "education", "cat", "orange", "sky", "elephant"]
result = [word for word in words if len(word) > 5 and word[0].lower() in "aeiou"]
print(result)

# Output: ['education', 'orange', 'elephant']
# এখানে:
# Word-এর Length 5-এর বেশি এবং প্রথম Letter Vowel হতে হবে।



# 🧠 AND বনাম OR
# AND:
# condition1 and condition2
# → দুটি Condition-ই True হতে হবে।

numbers = range(1, 11)
result = [number for number in numbers if number > 3 and number < 8]
print(result)


# OR:
# condition1 or condition2
# → যেকোনো একটি Condition True হলেই হবে।

numbers = range(1, 11)
result = [number for number in numbers if number < 3 or number > 8]
print(result)



# 9️⃣ Multiple Conditions-এর সাথে NOT
numbers = range(1, 11)
result = [number for number in numbers if not number % 2 == 0]
print(result)


# এখানে:
# number % 2 == 0 → Even
# not → সেটাকে উল্টে দিচ্ছে
# তাই শুধু Odd Number পাওয়া যাচ্ছে।



# 🔟 তিনটি Condition একসাথে
numbers = range(1, 51)
result = [
number
for number in numbers
if number > 10 and number < 40 and number % 2 == 0
]
print(result)

# Output:[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
# এখানে তিনটি Condition:
# 1. number > 10
# 2. number < 40
# 3. number Even
# তিনটিই True হতে হবে।



# 🧠 Normal Loop বনাম List Comprehension
# Normal Loop:
numbers = []
for number in range(1, 21):
    if number % 2 == 0 and number > 10:
        numbers.append(number)
print(numbers)


# List Comprehension:
numbers = [
number
for number in range(1, 21)
if number % 2 == 0 and number > 10
]
print(numbers)
