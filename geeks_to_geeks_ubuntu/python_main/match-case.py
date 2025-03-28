username = input('Enter username:')

match username:
    case 'John':
        print("Welcome Admin")
    case 'sim':
        print("Welcome User")
    case 'spongy':
        print('Welcome Guest')
    case _:
        print('Invalid username')