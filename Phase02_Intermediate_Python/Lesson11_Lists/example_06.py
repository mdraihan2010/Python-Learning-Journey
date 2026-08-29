# Start না দিলে :

numbers = [10, 20, 30, 40, 50]
print(numbers[:3])

# অর্থাৎ: শুরু → Index 3-এর আগে পর্যন্ত


# Stop না দিলে : 

numbers = [10, 20, 30, 40, 50]
print(numbers[2:])

# অর্থাৎ: Index 2 → শেষ পর্যন্ত


# পুরো List Copy করা

numbers = [10, 20, 30, 40, 50]
print(numbers[:])


# Step ব্যবহার করে Slicing
# Slicing-এর সম্পূর্ণ Syntax:
# list_name[start : stop : step]

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:6:2])



# Reverse করার জন্য Slicing

numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])