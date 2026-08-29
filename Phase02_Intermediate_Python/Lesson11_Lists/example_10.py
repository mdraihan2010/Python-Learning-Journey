# এখন আমরা Python List-এর কিছু গুরুত্বপূর্ণ Built-in Methods শিখব। 🚀

# ধরো আমাদের একটি List আছে:

numbers = [30, 10, 20, 10, 40]

# 1️⃣ append() : List-এর শেষে একটি নতুন Element যোগ করে।

numbers.append(50)
print(numbers)


# 2️⃣ insert() : নির্দিষ্ট Index-এ একটি Element যোগ করে।

numbers.insert(1, 100)
print(numbers)


# 3️⃣ extend() : একটি List-এর সাথে একাধিক Element যোগ করে।

numbers.extend([50, 60])
print(numbers)


# 4️⃣ remove() : নির্দিষ্ট Value Remove করে।

numbers.remove(20)
print(numbers)


# 5️⃣ pop() : শেষ Element Remove করে।

numbers.pop()
print(numbers)

# নির্দিষ্ট Index থেকেও Remove করা যায়:

numbers.pop(1)



# 6️⃣ clear() : পুরো List Empty করে দেয়।

numbers.clear()
print(numbers)


# 7️⃣ index() : কোনো Value-এর Index Position বের করে।

fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))


# 8️⃣ count() : কোনো Value List-এ কতবার আছে তা Count করে।

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))



# 9️⃣ sort() : List-এর Elementগুলো ছোট থেকে বড় বা Alphabetical Order-এ সাজায়।

numbers = [30, 10, 50, 20, 40]
numbers.sort()
print(numbers)

# Descending Order

numbers.sort(reverse=True)
print(numbers)



# 🔟 reverse() : List-এর বর্তমান Order উল্টে দেয়।

numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)


# 1️⃣1️⃣ copy() : একটি List-এর Copy তৈরি করে।

numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)



# append()  → শেষে একটি Element যোগ করে
# insert()  → নির্দিষ্ট Index-এ Element যোগ করে
# extend()  → একাধিক Element যোগ করে
# remove()  → Value দিয়ে Remove করে
# pop()     → Index বা শেষ Element Remove করে
# clear()   → সব Element Remove করে
# index()   → একটি Value-এর Index খুঁজে দেয়
# count()   → একটি Value কতবার আছে তা Count করে
# sort()    → List Sort করে
# reverse() → List-এর Order উল্টে দেয়
# copy()    → List-এর Copy তৈরি করে