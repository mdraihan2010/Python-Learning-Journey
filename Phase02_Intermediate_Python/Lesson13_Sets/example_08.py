# এখন আমরা Intersection of Sets শিখব। 🚀
# Intersection কী? : দুই বা একাধিক Set-এর মধ্যে যে Elementগুলো Common থাকে, সেগুলো বের করাকে Intersection বলে।

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# এখানে Common Element হলো: 30, 40
# তাই Intersection হবে: {30, 40}



# 1️⃣ intersection() Method ব্যবহার করে
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.intersection(set2)
print(result)



# 2️⃣ & Operator ব্যবহার করে : Intersection করার Shortcut হলো & Operator।

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1 & set2
print(result)

# অর্থাৎ:
# set1.intersection(set2)
# এবং:
# set1 & set2
# দুটোর Result একই। 😎



# 3️⃣ কোনো Common Element না থাকলে
set1 = {10, 20, 30}
set2 = {40, 50, 60}
result = set1.intersection(set2)
print(result)



# 4️⃣ তিনটি Set-এর Intersection
set1 = {10, 20, 30, 40}
set2 = {20, 30, 40, 50}
set3 = {30, 40, 60}
result = set1.intersection(set2, set3)
print(result)



# 5️⃣ Real-Life Example : ধরো দুইটি Course-এর Student List আছে।

python_students = {"Raihan", "Karim", "Rahim", "Hasan"}
data_science_students = {"Rahim", "Hasan", "Sakib"}
common_students = python_students.intersection(data_science_students)
print(common_students)