# এখন আমরা Symmetric Difference of Sets শিখব। 🚀
# Symmetric Difference কী? : দুইটি Set-এর মধ্যে যেসব Element Common নয়, অর্থাৎ যেগুলো শুধু একটি Set-এ আছে, সেগুলো বের করাকে Symmetric Difference বলে।

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# এখানে Common Element হলো: 30, 40
# তাই Common Element বাদ দিলে থাকবে: 10, 20, 50, 60
# অর্থাৎ Symmetric Difference হবে: {10, 20, 50, 60}



# 1️⃣ symmetric_difference() Method ব্যবহার করে
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.symmetric_difference(set2)
print(result)



# 2️⃣ ^ Operator ব্যবহার করে : Symmetric Difference-এর Shortcut হলো ^ Operator।
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1 ^ set2
print(result)

# অর্থাৎ:
# set1.symmetric_difference(set2)
# এবং:
# set1 ^ set2
# দুটোর Result একই। 😎

# সহজভাবে বুঝি 🧠
# Set1 → {10, 20, 30, 40}
# Set2 → {30, 40, 50, 60}
# Common → {30, 40}
# Symmetric Difference → {10, 20, 50, 60}
# অর্থাৎ: দুইটি Set-এর Common Element বাদ দিয়ে বাকি সব Element।



# 3️⃣ কোনো Common Element না থাকলে
set1 = {10, 20}
set2 = {30, 40}
print(set1 ^ set2)



# 4️⃣ দুটি একই Set হলে
set1 = {10, 20, 30}
set2 = {10, 20, 30}
print(set1 ^ set2)



# Real-Life Example

python_students = {"Raihan", "Karim", "Rahim"}
data_science_students = {"Rahim", "Hasan", "Sakib"}
result = python_students ^ data_science_students
print(result)