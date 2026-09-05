# একটি সংখ্যার multiplication table print করতে হবে।


number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(number, "x", multiplier, "=", result)