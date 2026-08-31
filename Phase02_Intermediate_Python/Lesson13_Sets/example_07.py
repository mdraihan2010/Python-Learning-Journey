# এখন আমরা বিস্তারিতভাবে Union of Sets শিখব। 🚀
# Union কী? : দুই বা একাধিক Set-এর সব Unique Element একসাথে করাকে Union বলে।

# set1 = {10, 20, 30}
# set2 = {30, 40, 50}

# দুই Set-এ 30 Common আছে। Union করলে 30 শুধু একবার থাকবে।
# set1 → {10, 20, 30}
# set2 → {30, 40, 50}
# Union → {10, 20, 30, 40, 50}



# 1️⃣ union() Method ব্যবহার করে
set1 = {10, 20, 30}
set2 = {30, 40, 50}
result = set1.union(set2)
print(result)



# 2️⃣ | Operator ব্যবহার করে : Union করার Shortcut হলো | Operator।
set1 = {10, 20, 30}
set2 = {30, 40, 50}
result = set1 | set2
print(result)

# অর্থাৎ:
# set1.union(set2)
# এবং:
# set1 | set2
# দুটোর Result একই।



# 3️⃣ তিনটি Set-এর Union
set1 = {10, 20}
set2 = {20, 30}
set3 = {30, 40}
result = set1.union(set2, set3)
print(result)



# 4️⃣ update() এবং Union : union() একটি নতুন Set Return করে এবং Original Set পরিবর্তন করে না।
set1 = {10, 20, 30}
set2 = {30, 40, 50}
result = set1.union(set2)
print("Set1 =", set1)
print("Result =", result)


# কিন্তু update() Original Set পরিবর্তন করে।
set1 = {10, 20, 30}
set2 = {30, 40, 50}
set1.update(set2)
print(set1)


# Complete Example

students_a = {"Raihan", "Karim", "Rahim"}
students_b = {"Rahim", "Hasan", "Sakib"}
all_students = students_a.union(students_b)
print(all_students)