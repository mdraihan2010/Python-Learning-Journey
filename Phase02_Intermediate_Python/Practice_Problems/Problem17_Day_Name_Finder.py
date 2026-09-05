# ১–৭ ইনপুট নিয়ে সপ্তাহের দিন print করতে হবে।


day_number = int(input("Enter day number (1-7): "))

match day_number:
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