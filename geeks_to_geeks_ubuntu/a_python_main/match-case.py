# about the days of the week with input
from pygame.surfarray import pixels_red

day = int(input("Type the number to see a day: "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")