# এখন আমরা Difference of Sets শিখব। 🚀
# Difference কী? : একটি Set-এ থাকা কিন্তু অন্য Set-এ না থাকা Elementগুলো বের করাকে Difference বলে।

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# এখানে set1-এ আছে কিন্তু set2-তে নেই: 10, 20
# তাই: set1 - set2 → {10, 20}



# 1️⃣ difference() Method ব্যবহার করে
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.difference(set2)
print(result)



# 2️⃣ - Operator ব্যবহার করে : Difference করার Shortcut হলো - Operator।
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1 - set2
print(result)

# অর্থাৎ:
# set1.difference(set2)
# এবং:
# set1 - set2
# দুটোর Result একই। 😎



# 3️⃣ Order খুব গুরুত্বপূর্ণ ⚠️ : Difference করার সময় Set-এর Order গুরুত্বপূর্ণ।
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1 - set2)
print(set2 - set1)



# 4️⃣ কোনো Difference না থাকলে
set1 = {10, 20, 30}
set2 = {10, 20, 30}
result = set1.difference(set2)
print(result)



# 5️⃣ Real-Life Example : ধরো একটি Python Course-এর Student আছে:

python_students = {"Raihan", "Karim", "Rahim", "Hasan"}
data_science_students = {"Rahim", "Hasan", "Sakib"}
result = python_students - data_science_students
print(result)