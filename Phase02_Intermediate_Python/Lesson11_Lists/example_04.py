# Negative Indexing কী?

# Positive Indexing বাম দিক থেকে শুরু হয়: 0 → 1 → 2 → 3
# আর Negative Indexing ডান দিক থেকে শুরু হয়: -4 → -3 → -2 → -1

fruits = ["Apple", "Banana", "Mango", "Orange"]

# Positive Index:   0         1         2         3
#                   ↓         ↓         ↓         ↓
#                 Apple    Banana    Mango     Orange
#                   ↑         ↑         ↑         ↑
# Negative Index:  -4        -3        -2        -1

# সবচেয়ে গুরুত্বপূর্ণ বিষয় হলো: শেষ Element-এর Negative Index সবসময় -1।

# শেষ Element Access করা


fruits = ["Apple", "Banana", "Mango"]
print(fruits[-1])