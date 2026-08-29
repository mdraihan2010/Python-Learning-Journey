# Recursion : যখন একটি Function নিজেকেই আবার Call করে, তখন তাকে Recursion বলে।
# Recursion-এ সাধারণত দুইটি অংশ থাকে।

# 1. Base Case : যে Condition-এ Function নিজেকে আর Call করবে না।
# 2. Recursive Case : যে অংশে Function আবার নিজেকে Call করে।

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)