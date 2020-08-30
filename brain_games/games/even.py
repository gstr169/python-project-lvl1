import prompt
from random import randint
from brain_games.constants import ANSWERS


def even_question() -> tuple:
    number = randint(0, 99)
    correct_answer = (number % 2) == 0
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if ANSWERS.get(answer) == correct_answer:
        return True, list(ANSWERS)[correct_answer], answer
    else:
        return False, list(ANSWERS)[correct_answer], answer
