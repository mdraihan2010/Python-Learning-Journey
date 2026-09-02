# এখন আমরা List Comprehension-এর মধ্যে একাধিক for ব্যবহার করা শিখব। 🚀
# এটাকে বলা হয় Nested List Comprehension। অর্থাৎ একটি List Comprehension-এর ভিতরে আরেকটি for loop ব্যবহার করা।



# 1️⃣ দুটি List-এর সব Combination
numbers1 = [1, 2, 3]
numbers2 = [4, 5]
result = [(number1, number2) for number1 in numbers1 for number2 in numbers2]
print(result)

# Output:
# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
# এখানে:
# প্রথমে number1 = 1
# তারপর numbers2-এর প্রতিটি Number-এর সাথে Pair তৈরি হচ্ছে।
# এরপর number1 = 2
# আবার numbers2-এর প্রতিটি Number-এর সাথে Pair তৈরি হচ্ছে।



# 2️⃣ দুটি Number-এর Multiplication
numbers1 = [1, 2, 3]
numbers2 = [10, 20]
result = [number1 * number2 for number1 in numbers1 for number2 in numbers2]
print(result)



# 3️⃣ দুটি List-এর প্রতিটি Element যোগ করা
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
result = [number1 + number2 for number1 in numbers1 for number2 in numbers2]
print(result)



# 4️⃣ Nested Loop-এর Normal Version বনাম List Comprehension
# Normal Loop:
result = []
for number1 in [1, 2, 3]:
    for number2 in [4, 5]:
        result.append((number1, number2))
print(result)


# List Comprehension:
result = [(number1, number2) for number1 in [1, 2, 3] for number2 in [4, 5]]
print(result)



# 5️⃣ Nested List থেকে সব Element বের করা
numbers = [[1, 2], [3, 4], [5, 6]]
result = [number for row in numbers for number in row]
print(result)

# Output:
# [1, 2, 3, 4, 5, 6]
# এখানে প্রথম for: row → [1, 2], [3, 4], [5, 6]
# দ্বিতীয় for: row-এর ভিতরের প্রতিটি number



# 6️⃣ Nested List-এর Square
numbers = [[1, 2], [3, 4], [5, 6]]
result = [number ** 2 for row in numbers for number in row]
print(result)



# 7️⃣ Nested List থেকে শুধু Even Number
numbers = [[1, 2], [3, 4], [5, 6]]
result = [number for row in numbers for number in row if number % 2 == 0]
print(result)


# এখানে প্রথমে Nested List-এর সব Number বের হচ্ছে।
# তারপর if condition দিয়ে শুধু Even Number নেওয়া হচ্ছে।



# 8️⃣ 2D List থেকে সব Number-এর Square
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
result = [number ** 2 for row in matrix for number in row]
print(result)