day = input("Enter a day: ")

match day:
    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case _:
        print("Invalid day")