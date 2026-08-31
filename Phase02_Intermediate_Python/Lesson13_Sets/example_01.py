# Set কী? : Set হলো Python-এর একটি Collection যেখানে একাধিক Value Store করা যায়। কিন্তু একই Value একাধিকবার থাকলেও Set Duplicate Value রাখে না।

# Set তৈরির Syntax : set_name = {value1, value2, value3}


# Set-এর গুরুত্বপূর্ণ বৈশিষ্ট্য 🧠

# 1. Duplicate Value Allow করে না
numbers = {10, 20, 10, 30}
print(numbers)



# 2. Set Unordered : List বা Tuple-এর মতো নির্দিষ্ট Position অনুযায়ী Element থাকে না।
fruits = {"Apple", "Banana", "Mango"}
print(fruits)



# 3. Indexing ব্যবহার করা যায় না
# List বা Tuple-এ: numbers[0] ব্যবহার করা যায়।
# কিন্তু Set-এ:
# numbers = {10, 20, 30}
# print(numbers[0])

# এটি Error দেবে: TypeError: 'set' object is not subscriptable .কারণ Set-এর কোনো Index নেই।



# 4. Set Mutable : Set-এর Element সরাসরি Index দিয়ে পরিবর্তন করা যায় না, কারণ Index নেই। কিন্তু নতুন Element যোগ বা পুরোনো Element Remove করা যায়।
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
