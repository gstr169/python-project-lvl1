from typing import Tuple
from random import randint, choice

OPERATIONS = (
    ('+', int.__add__),
    ('-', int.__sub__),
    ('*', int.__mul__),
)


def calc_game() -> Tuple[str, str]:
    number_a, number_b = randint(0, 99), randint(0, 99)
    operation_str, operation = choice(OPERATIONS)
    correct_answer = operation(number_a, number_b)
    question = f'Question: {number_a} {operation_str} {number_b}'
    return question, str(correct_answer)


calc_game.welcome_message = 'What is the result of the expression?'
