# Traffic light-এর color অনুযায়ী action print করতে হবে।


color = input("Enter traffic light color: ").lower()

match color:
    case "red":
        print("Stop")

    case "yellow":
        print("Wait")

    case "green":
        print("Go")

    case _:
        print("Invalid traffic light color")