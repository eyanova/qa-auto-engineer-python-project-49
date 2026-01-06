import random


def game_prime():

    question = random.randint(2, 300)
    sq_root = int(question ** 0.5)
    answer = 'yes'
    for i in range(2, sq_root + 1):
        if question % i == 0:
            answer = 'no'
            break
    return (str(question), answer)


INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'