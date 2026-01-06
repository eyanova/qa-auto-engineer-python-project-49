import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def engine(game, INSTRUCTION):

    greet()
    name = welcome_user()
    print(INSTRUCTION)
    count = 0
    for i in range(3):
        question, answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'. "
                  f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
            count += 1

    if count == 3:
        last_sent(name)


def last_sent(name):

    print(f'Congratulations, {name}!')
