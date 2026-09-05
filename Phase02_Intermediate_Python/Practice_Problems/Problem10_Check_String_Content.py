# string-এ শুধু digit, alphabet অথবা alphanumeric আছে কি না যাচাই করতে হবে।


user_string = input("Enter a string: ")

print("Only digits:", user_string.isdigit())
print("Only alphabets:", user_string.isalpha())
print("Alphanumeric:", user_string.isalnum())