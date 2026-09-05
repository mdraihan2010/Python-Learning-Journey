# একটি sentence-এর প্রতিটি word কতবার আছে তা গণনা করো।

sentence = "python is easy and python is popular"

words = sentence.split()
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)