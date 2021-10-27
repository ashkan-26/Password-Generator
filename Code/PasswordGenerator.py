from random import choice, choices, randrange
import string

print('Welcome to my password generator :)\n')
while True:
    try:

        length = int(input("""Enter the length of your password:
(in range of 8 to 16, type 0 if it doesn't matter.)

"""))
        if length == 0 : length = randrange(8,17)

        if (length<8 or length>16):
            raise ValueError("Invalid Entry!\n")
            x = input()
    except ValueError as ve:
        print(ve)
        continue


    # lower = 'abcdefghijklmnopqrstuvwxyz'
    # upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = string.ascii_letters
    string.digits
    number = string.digits
    character = '!@#$%&_/?'
    parts = [list(i) for i in [letter, number, character]]

    password = set({})
    # password = set(password)
    for i in range(length):
        Type = choices(parts, weights=(3, 2, 1.5))
        item = choice(choice(Type))
        password.add(item)

    Final = ''.join(password)
    print('\n'+Final)

    isContinue = input("\nPress Enter if you want to generate new password.\n")
    if isContinue!='': break