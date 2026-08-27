character = input("Enter a character: ")

match character:
    case "a" | "e" | "i" | "o" | "u":
        print("It is a vowel.")
    
    case _:
        print("It is not a vowel.")