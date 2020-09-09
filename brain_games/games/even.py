from typing import Tuple
from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_and_answer() -> Tuple[str, str]:
    number = randint(0, 99)
    is_even = (number % 2) == 0
    question = str(number)
    if is_even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
