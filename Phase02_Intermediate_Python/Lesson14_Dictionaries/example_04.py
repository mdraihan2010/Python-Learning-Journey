# এখন আমরা শিখব Dictionary-এর মধ্যে নতুন Key-Value Pair কীভাবে যোগ করতে হয়। 🚀

student = {
    "name": "Raihan",
    "age": 23
}

# এখন আমরা cgpa যোগ করতে চাই।
student["cgpa"] = 3.75
print(student)

# Output: {'name': 'Raihan', 'age': 23, 'cgpa': 3.75}
# এখানে:
# "cgpa" → Key
# 3.75   → Value


# 1️⃣ Basic Syntax : dictionary[key] = value
student = {}
student["name"] = "Raihan"
student["age"] = 23
student["department"] = "CSE"
print(student)

# Output: {'name': 'Raihan', 'age': 23, 'department': 'CSE'}



# 2️⃣ একসাথে কয়েকটি Item যোগ করা
student = {
    "name": "Raihan"
}
student["age"] = 23
student["cgpa"] = 3.75
student["department"] = "CSE"
print(student)



# 3️⃣ নতুন Key যোগ করার সময় [] ব্যবহার
student["email"] = "raihan@example.com"

# যদি "email" Key আগে না থাকে, তাহলে নতুন Key-Value Pair তৈরি হবে।



# 4️⃣ Existing Key দিলে কী হবে? ⚠️
student = {
    "name": "Raihan",
    "age": 23
}
student["age"] = 24

# এটি নতুন Key তৈরি করবে না। বরং পুরোনো Value পরিবর্তন করবে।

print(student)

# Output: {'name': 'Raihan', 'age': 24}

# তাই একই Syntax দিয়ে দুই ধরনের কাজ করা যায়: 
# Key না থাকলে → নতুন Item যোগ
# Key থাকলে → Value Update



# 5️⃣ update() ব্যবহার করে Item যোগ করা : একাধিক Key-Value Pair একসাথে যোগ করতে update() ব্যবহার করা যায়।
# student = {
#     "name": "Raihan"
# }
# student.update({
#     "age": 23,
#     "cgpa": 3.75,
#     "department": "CSE"
# })
# print(student)


# 🧠 [] vs update()
# একটি Item: 
student["age"] = 23

# একাধিক Item:
student.update({
    "age": 23,
    "cgpa": 3.75
})

# সহজভাবে: dictionary[key] = value দিয়ে একটি Item যোগ করা যায়, আর update() দিয়ে একসাথে একাধিক Item যোগ করা যায়।