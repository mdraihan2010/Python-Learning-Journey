# এখন আমরা List Comprehension-এর সাথে Nested List / 2D List নিয়ে Practice করব। 🚀
# 2D List মানে হলো একটি List-এর ভিতরে একাধিক List থাকা।



# 1️⃣ 2D List থেকে সব Element বের করা
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [number for row in numbers for number in row]
print(result)

# Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
# এখানে:
# প্রথম for → প্রতিটি Row নিচ্ছে।
# দ্বিতীয় for → সেই Row-এর প্রতিটি Number নিচ্ছে।
# অর্থাৎ:
# for row in numbers:
# for number in row:
# result.append(number)



# 2️⃣ 2D List থেকে শুধু Even Number
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [number for row in numbers for number in row if number % 2 == 0]
print(result)

# Output:[2, 4, 6, 8]
# প্রথমে সব Number-এর মধ্যে যাওয়া হচ্ছে।
# তারপর if condition দিয়ে শুধু Even Number নেওয়া হচ্ছে।



# 3️⃣ 2D List থেকে শুধু Odd Number
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [number for row in numbers for number in row if number % 2 != 0]
print(result)



# 4️⃣ সব Number-এর Square তৈরি করা
numbers = [
[1, 2],
[3, 4],
[5, 6]
]
result = [number ** 2 for row in numbers for number in row]
print(result)



# 5️⃣ 2D List-এর Positive Number
numbers = [
[-5, 10, -2],
[20, -3, 15],
[-8, 7, 0]
]
result = [number for row in numbers for number in row if number > 0]
print(result)

# Output:[10, 20, 15, 7]
# এখানে শুধু Positive Number নেওয়া হচ্ছে।
# 0 এবং Negative Number বাদ যাচ্ছে।



# 6️⃣ 2D List থেকে 10-এর বেশি Number
numbers = [
[5, 12, 8],
[20, 3, 15],
[7, 25, 10]
]
result = [number for row in numbers for number in row if number > 10]
print(result)



# 7️⃣ Multiple Conditions ব্যবহার করা
numbers = [
[5, 12, 8],
[20, 3, 15],
[7, 25, 10]
]
result = [
number
for row in numbers
for number in row
if number > 10 and number % 2 == 0
]
print(result)

# Output:[12, 20]
# এখানে দুটি Condition:
# 1. Number 10-এর বেশি হতে হবে।
# 2. Number Even হতে হবে।
# দুটি Condition-ই True হতে হবে।



# 8️⃣ 2D List থেকে String-এর Length বের করা
words = [
["cat", "dog"],
["elephant", "fox"],
["tiger", "lion"]
]
result = [len(word) for row in words for word in row]
print(result)



# 9️⃣ 2D List থেকে Long Words বের করা
words = [
["cat", "elephant"],
["dog", "tiger"],
["lion", "giraffe"]
]
result = [
word
for row in words
for word in row
if len(word) > 4
]
print(result)



# 🔟 2D List-এর প্রতিটি Number Double করা
numbers = [
[1, 2, 3],
[4, 5, 6]
]
result = [number * 2 for row in numbers for number in row]
print(result)



# 1️⃣1️⃣ Nested List থেকে নতুন 2D List তৈরি করা
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [[number * 2 for number in row] for row in numbers]
print(result)

# Output:[[2, 4, 6], [8, 10, 12], [14, 16, 18]]
# লক্ষ্য করো:
# এখানে আমরা একটি নতুন 2D List তৈরি করছি।
# ভিতরের Comprehension:
# [number * 2 for number in row]
# বাইরের Comprehension:
# [ ... for row in numbers]



# 1️⃣2️⃣ 2D List-এর প্রতিটি Number-এর Square
numbers = [
[1, 2, 3],
[4, 5, 6]
]
result = [[number ** 2 for number in row] for row in numbers]
print(result)

# Output:[[1, 4, 9], [16, 25, 36]]
# এখানে আগের Example-এর মতো আমরা List Flatten করছি না।
# বরং প্রতিটি Row আলাদা রেখেই নতুন 2D List তৈরি করছি।



# 🧠 Flattening বনাম নতুন 2D List
# Flattening:
numbers = [
[1, 2],
[3, 4],
[5, 6]
]
result = [number for row in numbers for number in row]
print(result)


# নতুন 2D List:
result = [[number * 2 for number in row] for row in numbers]
print(result)

# Output:[[2, 4], [6, 8], [10, 12]]
# প্রথমটিতে → সব Row একত্র হয়ে একটি List।
# দ্বিতীয়টিতে → Row structure ঠিক থাকে।



# 1️⃣3️⃣ Matrix-এর প্রতিটি Element-এর সাথে 10 যোগ করা
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [[number + 10 for number in row] for row in matrix]
print(result)



# 1️⃣4️⃣ Matrix থেকে শুধু Even Number রেখে 0 করা
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [
[number if number % 2 == 0 else 0 for number in row]
for row in matrix
]
print(result)

# Output:[[0, 2, 0], [4, 0, 6], [0, 8, 0]]
# এখানে:
# Even হলে → Number
# Odd হলে → 0
# এবং পুরো Row structure বজায় থাকছে।
