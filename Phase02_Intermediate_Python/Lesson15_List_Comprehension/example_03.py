# এখন আমরা List Comprehension-এর মধ্যে if-else ব্যবহার করা শিখব। 🚀
# if-else ব্যবহার করলে: [expression_if_true if condition else expression_if_false for item in iterable]
# এখানে প্রতিটি Element-এর জন্য Condition Check হবে এবং Condition অনুযায়ী একটি Value নতুন List-এ যাবে।



# 1️⃣ Even / Odd নির্ণয়
numbers = range(1, 11)
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(result)

# এখানে:
# number % 2 == 0 → Condition
# Condition True হলে → "Even"
# Condition False হলে → "Odd"



# 2️⃣ Even হলে Number, Odd হলে 0
numbers = range(1, 11)
result = [number if number % 2 == 0 else 0 for number in numbers]
print(result)

# এখানে Even Number হলে Number-টি List-এ যোগ হচ্ছে।
# আর Odd Number হলে তার পরিবর্তে 0 যোগ হচ্ছে।



# 3️⃣ Positive / Negative
numbers = [-5, 10, -2, 20, 0, 15]
result = ["Positive" if number > 0 else "Negative" for number in numbers]
print(result)

# এখানে Number 0 হলে Condition False হবে, তাই "Negative" দেখাবে।



# 4️⃣ Pass / Fail
marks = [35, 80, 42, 20, 90, 55]
result = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print(result)



# 5️⃣ Adult / Minor
ages = [12, 18, 25, 15, 30]
result = ["Adult" if age >= 18 else "Minor" for age in ages]
print(result)



# 6️⃣ Positive হলে Number, Negative হলে 0
numbers = [-10, 20, -5, 30, -15, 40]
result = [number if number > 0 else 0 for number in numbers]
print(result)



# 7️⃣ Even হলে Square, Odd হলে Number
numbers = range(1, 11)
result = [number ** 2 if number % 2 == 0 else number for number in numbers]
print(result)



# 8️⃣ String-এর ক্ষেত্রে if-else
words = ["apple", "banana", "cat", "elephant"]
result = ["Long" if len(word) > 5 else "Short" for word in words]
print(result)



# 🧠 শুধু if বনাম if-else
# শুধু if:

numbers = range(1, 11)
result = [number for number in numbers if number % 2 == 0]
print(result)

# এখানে শুধু Even Number List-এ যাচ্ছে। Odd Number বাদ পড়ে যাচ্ছে।


# if-else:

numbers = range(1, 11)
result = [number if number % 2 == 0 else 0 for number in numbers]
print(result)

# এখানে কোনো Number বাদ যাচ্ছে না। Even হলে Number এবং Odd হলে 0 List-এ যাচ্ছে।