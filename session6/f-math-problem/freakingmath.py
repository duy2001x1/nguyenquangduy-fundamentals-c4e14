from random import *
from calc import *

def generate_quiz():
    x = randint(0, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    error = randint(-1, 1)
    result = evaluate(x, y, op) + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_result = evaluate(x, y, op)
    if user_choice:
        return true_result == result
    else:
        return not true_result == result
    
    # return user_choice == (true_result == result)
