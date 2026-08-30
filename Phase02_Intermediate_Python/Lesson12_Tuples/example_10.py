# List-এর অনেক Methods থাকলেও Tuple Immutable হওয়ার কারণে Tuple-এর Method খুব কম। মূলত দুটি গুরুত্বপূর্ণ Method আছে:
# 1. count()
# 2. index()



# 1️⃣ count() Method : count() ব্যবহার করে কোনো Value Tuple-এর মধ্যে কতবার আছে তা জানা যায়।
# Syntax : tuple_name.count(value)

numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))

# আরেকটি Example:
fruits = ("Apple", "Banana", "Mango", "Apple")
print(fruits.count("Apple"))



# 2️⃣ index() Method : index() ব্যবহার করে কোনো Value Tuple-এর কোন Index-এ আছে তা জানা যায়।
# Syntax : tuple_name.index(value)

fruits = ("Apple", "Banana", "Mango")
print(fruits.index("Banana"))


# একই Value একাধিকবার থাকলে কী হবে? : index() সবসময় প্রথম পাওয়া Value-এর Index Return করে।
numbers = (10, 20, 10, 30, 10)
print(numbers.index(10))


# Value না থাকলে কী হবে? ⚠️ তাহলে Error হবে: ValueError: tuple.index(x): x not in tuple
numbers = (10, 20, 30)
print(numbers.index(50))


# Complete Example

numbers = (10, 20, 10, 30, 10, 40)
print("Count of 10 =", numbers.count(10))
print("Index of 30 =", numbers.index(30))