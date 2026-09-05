# একটি file-এর শেষে নতুন data append করো।

file = open("data.txt", "a")

file.write("\nThis is appended data.")

file.close()

print("Data appended successfully.")