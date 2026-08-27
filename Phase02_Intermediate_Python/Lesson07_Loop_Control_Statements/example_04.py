# continue → বর্তমান Iteration Skip
# break    → পুরো Loop Stop



# Basic Syntax

# for variable in sequence:
#     if condition:
#         continue

#     statement



# অথবা while Loop-এ:

# while condition:
#     if condition:
#         continue

#     statement

for number in range(1, 6):
    if number == 3:
        continue

    print(number)