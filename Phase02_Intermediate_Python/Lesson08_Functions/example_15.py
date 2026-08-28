# global Keyword : যদি সত্যিই Function-এর ভিতর থেকে Global Variable পরিবর্তন করতে চাও, তাহলে global Keyword ব্যবহার করা যায়।


number = 10

def change_number():
    global number

    number = 20

change_number()

print(number)
