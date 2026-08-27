# Basic Syntax

# match variable:
#     case value1:
#         statement

#     case value2:
#         statement

#     case value3:
#         statement

#     case _:
#         statement

# এখানে:
# match → যে Variable-এর Value পরীক্ষা করব।
# case → কোন Value-এর সাথে মিলছে তা পরীক্ষা করবে।
# _ → কোনো case-এর সাথে না মিললে Default Case হিসেবে কাজ করবে।

day = int(input("Enter a day number: "))

match day:
    case 1:
        print("Saturday")

    case 2:
        print("Sunday")

    case 3:
        print("Monday")

    case 4:
        print("Tuesday")

    case 5:
        print("Wednesday")

    case 6:
        print("Thursday")

    case 7:
        print("Friday")

    case _:
        print("Invalid day number")