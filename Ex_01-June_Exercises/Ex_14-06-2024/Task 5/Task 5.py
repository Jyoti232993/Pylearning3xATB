numbers = int(input("Enter any number:"))
# 3.10

match numbers:
    case 1:
        print("You have entered 1.")
    case 2:
        print("You have entered 2.")
    case 3:
        print("You have entered 3.")
    case 4:
        print("You have entered 4.")
    case 5:
        print("You have entered 5.")
    case 6:
        print("You have entered 6.")
    case _:
        print("No idea")



def allowed_to_attend_python_class(name):

    match name:
        case "DELL":
            print("DELL is allowed.")

        case "Shubham":
            print("Shubham is allowed.")

        case "Pallavi":
             print("Pallavi is allowed.")

        case _:
            print("Not allowed.")

allowed_to_attend_python_class("Shubham")




