# file না পাওয়া গেলে FileNotFoundError handle করো।

try:
    file = open("data.txt", "r")

    data = file.read()

    file.close()

    print(data)
except FileNotFoundError:
    print("Error: File not found.")