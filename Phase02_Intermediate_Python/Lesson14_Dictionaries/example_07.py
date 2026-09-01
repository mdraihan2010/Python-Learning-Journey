# এখন আমরা Dictionary-এর সবচেয়ে গুরুত্বপূর্ণ Methods শিখব। 🚀

student = {
    "name": "Raihan",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.75
}



# 1️⃣ keys() : Dictionary-এর সব Key বের করতে keys() ব্যবহার করা হয়।
print(student.keys())



# 2️⃣ values() : Dictionary-এর সব Value বের করতে values() ব্যবহার করা হয়।
print(student.values())



# 3️⃣ items() : সব Key-Value Pair একসাথে বের করতে items() ব্যবহার করা হয়।
print(student.items())



# 4️⃣ get() : নির্দিষ্ট Key-এর Value Access করতে get() ব্যবহার করা যায়।
print(student.get("name"))

# Key না থাকলে:
print(student.get("phone"))

# Default Value-ও দেওয়া যায়:
print(student.get("phone", "Not Available"))



# 5️⃣ update() : Dictionary-তে নতুন Item যোগ অথবা Existing Value Update করতে update() ব্যবহার করা যায়।
student.update({
    "age": 24,
    "cgpa": 3.80
})
print(student)



# 6️⃣ pop() : নির্দিষ্ট Key-এর Key-Value Pair Remove করে।
student.pop("age")
print(student)



# 7️⃣ popitem() : শেষ Key-Value Pair Remove করে।
student.popitem()
print(student)



# 8️⃣ clear() : Dictionary-এর সব Item Remove করে।
student.clear()
print(student)



# 9️⃣ copy() : Dictionary-এর একটি Copy তৈরি করে।
student = {
    "name": "Raihan",
    "age": 23
}
new_student = student.copy()
print(new_student)



# 🧠 সবচেয়ে গুরুত্বপূর্ণ Methods
# keys()      → সব Key
# values()    → সব Value
# items()     → সব Key-Value Pair
# get()       → Key দিয়ে Value Access
# update()    → Add / Update
# pop()       → নির্দিষ্ট Key Remove
# popitem()   → শেষ Item Remove
# clear()     → সব Item Remove
# copy()      → Dictionary Copy