import random


def game_progression():

    start = random.randint(1, 15)
    length = random.randint(6, 10)
    step = random.randint(1, 15)
    question, answer = current_el(start, length, step)
    return (str(question), str(answer))


INSTRUCTION = 'What number is missing in the progression?'


def current_el(start, length, step):

    numbers = [start]
    for i in range(length):
        number = start + step
        numbers.append(str(number))
        start = number
    empty = random.randint(0, length - 1)
    answer = numbers[empty]
    numbers[empty] = '..'
    question = " ".join(map(str, numbers))
    return (str(question), str(answer))
