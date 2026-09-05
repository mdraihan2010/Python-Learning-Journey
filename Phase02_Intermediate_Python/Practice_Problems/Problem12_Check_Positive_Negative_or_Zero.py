# একটি সংখ্যা positive, negative নাকি zero তা নির্ণয় করতে হবে।


number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")