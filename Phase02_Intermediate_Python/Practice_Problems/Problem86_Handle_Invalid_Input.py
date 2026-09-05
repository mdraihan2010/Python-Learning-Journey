# user ভুল input দিলে ValueError handle করো।

try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid input. Please enter a valid number.")