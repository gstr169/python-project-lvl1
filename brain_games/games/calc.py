from typing import Tuple
from random import randint, choice

OPERATIONS = [
    ('+', int.__add__),
    ('-', int.__sub__),
    ('*', int.__mul__),
]

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer() -> Tuple[str, str]:
    number_a, number_b = randint(0, 99), randint(0, 99)
    sign, operation = choice(OPERATIONS)
    correct_answer = str(operation(number_a, number_b))
    question = f'{number_a} {sign} {number_b}'
    return question, correct_answer
