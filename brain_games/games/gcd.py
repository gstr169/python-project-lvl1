from typing import Tuple
from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer() -> Tuple[str, str]:
    number_a, number_b = randint(0, 99), randint(0, 99)
    correct_answer = str(gcd(number_a, number_b))
    question = f'{number_a} {number_b}'
    return question, correct_answer
