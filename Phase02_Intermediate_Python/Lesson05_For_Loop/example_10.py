# Nested Loop Concepts

# Outer Loop একবার
#     ↓
# Inner Loop সম্পূর্ণ চলবে
#     ↓
# Outer Loop আবার চলবে
#     ↓
# Inner Loop আবার সম্পূর্ণ চলবে


for i in range(1, 4):
    for j in range(1, 3):
        print("i =", i, "j =", j)