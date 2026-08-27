color = input("Enter a color: ")

match color:
    case "red":
        print("Stop")

    case "green":
        print("Go")

    case "yellow":
        print("Wait")

    case _:
        print("Unknown color")