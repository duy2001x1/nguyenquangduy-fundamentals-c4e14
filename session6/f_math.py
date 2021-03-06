# import calc
#
# result = calc.evaluate(1, 3, '*')
# print(result)

# from calc import evaluate
#
# result = evaluate(1, 3, '-')
# print(result)

# from calc import *
#
# result = evaluate(2, 4, '/')
# print(result)

from calc import *
from random import *

x = randint(0, 10)
y = randint(1, 10)
op = choice(['+'] * 50 + ['-'] * 25 + ['*'] * 10 + ['/'] * 15)
error = randint(-1, 1)
result = evaluate(x, y, op) + error
print('{0} {1} {2} = {3}'.format(x, op, y, result))

answer = input("Your answer: (Y/N)? ").upper()
if answer == 'Y':
    if error == 0:
        print('yay')
    else:
        print('nah')
else:
    if error == 0:
        print('nah')
    else:
        print('yay')
