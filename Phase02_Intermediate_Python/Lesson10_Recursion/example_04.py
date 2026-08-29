# Base Case হলো সেই Condition যেখানে Recursive Function নিজেকে আর Call করবে না এবং Stop করবে।


def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)

countdown(5)


# এখানে:
# if number == 0:
#     return
# হলো Base Case। কারণ number যখন 0 হবে, তখন Function আর নিজেকে Call করবে না।