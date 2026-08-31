# এখন আমরা শিখব Set-এর মধ্যে নতুন Element কীভাবে যোগ করতে হয়। 🚀


# Set-এ Element যোগ করার জন্য প্রধানত দুইটি Method ব্যবহার করা হয়:
# 1. add()
# 2. update()


# 1️⃣ add() Method : add() ব্যবহার করে Set-এ একটি নতুন Element যোগ করা হয়।
# Syntax : set_name.add(value)

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)


# একই Value আবার Add করলে কী হবে?
numbers = {10, 20, 30}
numbers.add(20)
print(numbers)

# কারণ Set Duplicate Value রাখে না। তাই নতুন করে কিছু Add হবে না।


# String Add করা
fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)



# 2️⃣ update() Method : update() ব্যবহার করে Set-এ একাধিক Element যোগ করা যায়।
# Syntax : set_name.update(iterable)

numbers = {10, 20, 30}
numbers.update([40, 50, 60])
print(numbers)

# এখানে একটি List থেকে একাধিক Element Set-এ যোগ হয়েছে।


# Tuple ব্যবহার করে update()
numbers = {10, 20, 30}
numbers.update((40, 50, 60))
print(numbers)


# অন্য একটি Set যোগ করা
set1 = {10, 20, 30}
set2 = {40, 50, 60}
set1.update(set2)
print(set1)
