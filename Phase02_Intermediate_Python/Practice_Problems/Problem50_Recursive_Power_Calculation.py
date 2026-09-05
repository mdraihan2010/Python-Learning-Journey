# recursion ব্যবহার করে base^power নির্ণয় করতে হবে।

def calculate_power(base, power):
    if power == 0:
        return 1

    return base * calculate_power(base, power - 1)


base = float(input("Enter the base: "))
power = int(input("Enter the power: "))

result = calculate_power(base, power)

print("Result:", result)