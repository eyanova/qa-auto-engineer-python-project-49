import random


def game_even():

    question = random.randint(1, 15)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'