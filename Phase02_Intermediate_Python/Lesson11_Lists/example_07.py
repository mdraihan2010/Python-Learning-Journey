# List Element Update কী? : List হলো Mutable, অর্থাৎ List তৈরি করার পর এর ভিতরের Element পরিবর্তন করা যায়।

# Basic Syntax
# list_name[index] = new_value

# এখানে:
# list_name → যে List পরিবর্তন করবে
# index     → কোন Element পরিবর্তন করবে
# new_value → নতুন Value

# Example 1️⃣

numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers)


# Example 2️⃣ String List

students = ["Raihan", "Rahim", "Karim"]
students[0] = "Sakib"
print(students)


# একাধিক Element Update করা

numbers = [10, 20, 30, 40, 50]
numbers[1:3] = [100, 200]
print(numbers)