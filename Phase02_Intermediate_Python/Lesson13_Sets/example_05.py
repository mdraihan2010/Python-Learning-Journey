# এখন আমরা শিখব Set থেকে Element কীভাবে Remove করতে হয়। 🚀

# Set থেকে Element Remove করার জন্য কয়েকটি গুরুত্বপূর্ণ Method আছে:
# 1. remove()
# 2. discard()
# 3. pop()
# 4. clear()


# 1️⃣ remove() Method : remove() ব্যবহার করে নির্দিষ্ট একটি Value Set থেকে Remove করা যায়।
# Syntax : set_name.remove(value)

numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)


# Value না থাকলে কী হবে? ⚠️
numbers = {10, 20, 30}
numbers.remove(50)

# এটি Error দেবে: KeyError: 50
# কারণ 50 Set-এর মধ্যে নেই।



# 2️⃣ discard() Method : discard()-ও নির্দিষ্ট Value Remove করে।
numbers = {10, 20, 30}
numbers.discard(20)
print(numbers)


# Value না থাকলে?
numbers = {10, 20, 30}
numbers.discard(50)
print(numbers)

# এখানে কোনো Error হবে না। 😎


# 3️⃣ pop() Method : pop() ব্যবহার করে Set থেকে একটি Element Remove করা যায়।
numbers = {10, 20, 30, 40}
removed = numbers.pop()
print("Removed:", removed)
print("Remaining Set:", numbers)

# ⚠️ খুব গুরুত্বপূর্ণ বিষয়: Set Unordered হওয়ায় pop() কোন Element Remove করবে, তার উপর নির্ভর করা উচিত নয়। 
# List-এর মতো Set-এ pop(1) ব্যবহার করা যায় না।



# 4️⃣ clear() Method : clear() ব্যবহার করে Set-এর সব Element Remove করা যায়।
numbers = {10, 20, 30}
numbers.clear()
print(numbers)



# Complete Example

numbers = {10, 20, 30, 40, 50}
numbers.remove(20)
numbers.discard(100)
numbers.pop()
print(numbers)

# এখানে:
# remove(20)    → 20 Remove করবে
# discard(100)  → 100 না থাকলেও Error হবে না
# pop()         → একটি Element Remove করবে