import random


def game_gcd():

    a = random.randint(1, 50)
    b = random.randint(1, 50)
    question = f'{a} {b}'
    if b == 0:
        answer = a
    else:
        while b != 0:
            a, b = b, a % b
        answer = a
    return (question, str(answer))


INSTRUCTION = 'Find the greatest common divisor of given numbers.'