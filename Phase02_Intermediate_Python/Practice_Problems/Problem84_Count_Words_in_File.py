# একটি file-এ মোট কতটি word আছে তা গণনা করো।

file = open("data.txt", "r")

data = file.read()

file.close()

words = data.split()

print("Total words:", len(words))