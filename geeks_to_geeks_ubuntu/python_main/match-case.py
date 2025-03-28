# username = input('Enter username:')
#
# match username:
#     case 'John':
#         print("Welcome Admin")
#     case 'sim':
#         print("Welcome User")
#     case 'spongy':
#         print('Welcome Guest')
#     case _:
#         print('Invalid username')

day = int(input('Enter the number of the day in week:'))

match day:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('friday')
    case 7:
        print('')