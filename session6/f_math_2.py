from random import randint

x = randint(1, 10)
y = randint(1, 10)

error = randint(-1, 1)

operation = randint(0, 100)

if operation <= 50:
    result = x + y + error
    print('{0} + {1} = {2}'.format(x, y, result))

    answer = input('Y/N? '). lower()

    if answer == 'y':
        if result == x + y:
            print('yay')
        else:
            print('nah')
    elif answer == 'n':
        if result == x + y:
            print('nah')
        else:
            print('yay')

elif operation <= 75:
    result = x - y + error
    print('{0} - {1} = {2}'.format(x, y, result))

    answer = input('Y/N? '). lower()

    if answer == 'y':
        if result == x - y:
            print('yay')
        else:
            print('nah')
    elif answer == 'n':
        if result == x - y:
            print('nah')
        else:
            print('yay')

elif operation <= 85:
    result = x * y + error
    print('{0} * {1} = {2}'.format(x, y, result))

    answer = input('Y/N? '). lower()

    if answer == 'y':
        if result == x * y:
            print('yay')
        else:
            print('nah')
    elif answer == 'n':
        if result == x * y:
            print('nah')
        else:
            print('yay')

else:
    result = x / y + error
    print('{0} / {1} = {2}'.format(x, y, result))

    answer = input('Y/N? '). lower()

    if answer == 'y':
        if result == x / y:
            print('yay')
        else:
            print('nah')
    elif answer == 'n':
        if result == x / y:
            print('nah')
        else:
            print('yay')
