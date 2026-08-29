# Sum of Numbers Using Recursion


def sum_numbers(number):

    if number == 1:
        return 1

    return number + sum_numbers(number - 1)

result = sum_numbers(5)

print(result)