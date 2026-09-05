# একটি text file তৈরি করে সেখানে data লিখো।

file = open("data.txt", "w")

file.write("Hello, Python!\n")
file.write("This is my first file.")

file.close()

print("Data written successfully.")