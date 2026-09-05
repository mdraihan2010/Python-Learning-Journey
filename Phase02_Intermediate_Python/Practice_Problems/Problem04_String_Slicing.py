# একটি string-এর নির্দিষ্ট অংশ slicing করে print করতে হবে।


user_string = input("Enter a string: ")

start_index = int(input("Enter starting index: "))
end_index = int(input("Enter ending index: "))

sliced_string = user_string[start_index:end_index]

print("Sliced string:", sliced_string)