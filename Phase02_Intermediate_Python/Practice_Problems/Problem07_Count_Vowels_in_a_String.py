# একটি string-এ কতগুলো vowel আছে তা গণনা করতে হবে।


user_string = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for character in user_string:
    if character in vowels:
        vowel_count += 1

print("Total vowels:", vowel_count)