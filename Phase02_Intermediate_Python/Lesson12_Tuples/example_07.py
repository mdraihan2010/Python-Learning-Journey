# এখন একটি খুব গুরুত্বপূর্ণ বিষয় শিখব। Tuple Immutable, অর্থাৎ Tuple তৈরি হওয়ার পরে এর Element সরাসরি পরিবর্তন করা যায় না। 🚀

# fruits = ("Apple", "Banana", "Mango")

# এখন যদি আমরা "Banana" পরিবর্তন করে "Orange" করতে চাই:

# fruits[1] = "Orange"

# তাহলে Error হবে: TypeError: 'tuple' object does not support item assignment
# কারণ Tuple-এর Element সরাসরি Update করা যায় না।



# Tuple-কে আগে List-এ Convert করব, তারপর পরিবর্তন করব, এরপর আবার Tuple-এ Convert করব।

# Step 1: Tuple তৈরি
fruits = ("Apple", "Banana", "Mango")


# Step 2: List-এ Convert করা
fruits_list = list(fruits)
print(fruits_list)

# এখন List হবে: ['Apple', 'Banana', 'Mango']


# Step 3: Element Update করা
fruits_list[1] = "Orange"

# এখন List হবে: ['Apple', 'Orange', 'Mango']


# Step 4: আবার Tuple-এ Convert করা
fruits = tuple(fruits_list)
print(fruits)


# Complete Code

fruits = ("Apple", "Banana", "Mango")
fruits_list = list(fruits)
fruits_list[1] = "Orange"
fruits = tuple(fruits_list)
print(fruits)



















