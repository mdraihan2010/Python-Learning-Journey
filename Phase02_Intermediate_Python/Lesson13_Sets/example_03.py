# এখন আমরা Python Set-এর গুরুত্বপূর্ণ Properties সম্পর্কে জানব। 🚀


# 1️⃣ Set Duplicate Value রাখে না : Set-এর সবচেয়ে গুরুত্বপূর্ণ Property হলো একই Value একাধিকবার থাকলেও Set শুধু একবার রাখে।
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)



# 2️⃣ Set Unordered : Set-এর Elementগুলোর কোনো নির্দিষ্ট Order নেই।
fruits = {"Apple", "Banana", "Mango", "Orange"}
print(fruits)



# 3️⃣ Set-এ Indexing নেই : 
# List এবং Tuple-এ আমরা লিখতে পারি: numbers[0]
# কিন্তু Set-এ এটি সম্ভব নয়।

# numbers = {10, 20, 30}
# print(numbers[0])

# Error: TypeError: 'set' object is not subscriptable
# কারণ Set-এর কোনো Index নেই।



# 4️⃣ Set Mutable : Set তৈরি হওয়ার পরে নতুন Element যোগ করা যায়।
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# আবার Element Remove-ও করা যায়।
numbers.remove(20)
print(numbers)

# তাই Set নিজে Mutable।




# 5️⃣ Set-এর Element অবশ্যই Immutable হতে হবে ⚠️ : Set-এর ভিতরে সাধারণত এমন Value রাখা যায় যেগুলো পরিবর্তনযোগ্য নয়।
numbers = {10, 20, 30}
fruits = {"Apple", "Banana"}

# কিন্তু একটি List সরাসরি Set-এর Element হতে পারে না।
data = {10, [20, 30]}

# এটি Error দেবে: TypeError: unhashable type: 'list'
# কারণ List Mutable।



# 6️⃣ Set Mixed Data Types Store করতে পারে
data = {"Raihan", 23, 3.75, True}
print(data)

# একটি Set-এর মধ্যে থাকতে পারে:
# String
# Integer
# Float
# Boolean