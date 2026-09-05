# user-এর কাছ থেকে বারবার input নিতে হবে।
# user "exit" লিখলে input নেওয়া বন্ধ হবে।

while True:
    user_input = input("Enter something (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Input ended.")
        break

    print("You entered:", user_input)