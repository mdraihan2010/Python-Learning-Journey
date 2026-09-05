# একটি নির্দিষ্ট word খুঁজে অন্য word দিয়ে replace করতে হবে।


user_string = input("Enter a string: ")
search_word = input("Enter the word to find: ")
replace_word = input("Enter the replacement word: ")

updated_string = user_string.replace(search_word, replace_word)

print("Updated string:", updated_string)