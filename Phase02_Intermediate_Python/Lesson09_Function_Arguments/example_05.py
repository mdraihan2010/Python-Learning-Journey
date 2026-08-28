# দুই ধরনের Variable-Length Arguments আছে:

# 1. *args   → Multiple Positional Arguments
# 2. **kwargs → Multiple Keyword Arguments

# *args ব্যবহার করা হয় যখন Function কতগুলো Positional Arguments গ্রহণ করবে তা আগে থেকে জানা নেই।

# Basic Example


def show_numbers(*numbers):
    print(numbers)


show_numbers(10, 20)

show_numbers(10, 20, 30)

show_numbers(10, 20, 30, 40, 50)