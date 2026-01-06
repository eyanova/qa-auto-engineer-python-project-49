import random


def game_calc():

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    sign = random.choice(['+', '-', '*'])
    if sign == '+':
        answer = a + b
    elif sign == '-':
        answer = a - b
    elif sign == '*':
        answer = a * b
    question = f'{a} {sign} {b}'
    return (question, str(answer))


INSTRUCTION = 'What is the result of the expression?'
