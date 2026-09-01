# এখন আমরা শিখব Dictionary-এর আগে থেকে থাকা Value কীভাবে Update বা পরিবর্তন করতে হয়। 🚀

student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.50
}

# এখন CGPA 3.50 থেকে 3.75 করতে চাই।
student["cgpa"] = 3.75
print(student)

# Output: {'name': 'Raihan', 'age': 23, 'cgpa': 3.75}
# এখানে "cgpa" Key আগে থেকেই ছিল, তাই তার Value Update হয়েছে।



# 1️⃣ Basic Syntax : dictionary[key] = new_value
student["age"] = 24

# এখানে "age" আগে থেকেই ছিল, তাই 23 পরিবর্তন হয়ে 24 হয়েছে।



# 2️⃣ update() দিয়ে Update করা : একটি বা একাধিক Key-এর Value Update করতে update() ব্যবহার করা যায়।
student = {
    "name": "Raihan",
    "age": 23,
    "cgpa": 3.50
}
student.update({
    "age": 24,
    "cgpa": 3.75
})
print(student)



# 3️⃣ একই Syntax-এ Add এবং Update
student["cgpa"] = 3.75

# যদি "cgpa" Key না থাকে: → নতুন Key-Value Pair যোগ হবে
# যদি "cgpa" Key আগে থেকেই থাকে: → পুরোনো Value Update হবে

# অর্থাৎ:
# dictionary[key] = value
# দিয়ে Add এবং Update দুটোই করা যায়।



# 4️⃣ Nested Dictionary Update
student = {
    "info": {
        "name": "Raihan",
        "age": 23
    }
}

#এখন Age Update করতে:
student["info"]["age"] = 24
print(student)