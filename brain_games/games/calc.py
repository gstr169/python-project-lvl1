import prompt
from random import randint, choice
from brain_games.constants import OPERATIONS


def calc_question() -> tuple:
    number_a, number_b = randint(0, 99), randint(0, 99)
    operation_str, operation = choice(OPERATIONS)
    correct_answer = operation(number_a, number_b)
    print(f'Question: {number_a} {operation_str} {number_b}')
    answer = prompt.string('Your answer: ')
    if int(answer) == correct_answer:
        return True, correct_answer, answer
    else:
        return False, correct_answer, answer

