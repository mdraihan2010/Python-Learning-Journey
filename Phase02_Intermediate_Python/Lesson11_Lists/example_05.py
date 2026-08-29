# List Slicing কী? : List-এর একটি নির্দিষ্ট অংশ বা একাধিক Element একসাথে Access করাকে List Slicing বলে।
# Basic Syntax
# list_name[start : stop]

# এখানে:
# start → কোন Index থেকে শুরু হবে
# stop → কোন Index-এর আগে শেষ হবে

# ⚠️ সবচেয়ে গুরুত্বপূর্ণ বিষয়: Stop Index-এর Element Slicing-এর মধ্যে Include হয় না।

# Example

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits[1:3])