# from random import randint, choice
def evaluate(x, y, op):
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    else:
        result = x / y
    return result

# x = randint(0, 10)
# y = randint(1, 10)
# op = choice(['+', '-', '*', '/'])
# print(x, op, y)
#
# z = evaluate(x, y, op)
#
# print(z)
# # print(z + randint(-1, 1))
