from typing import Tuple
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int) -> bool:
    if n < 0:
        return False
    if n in (0, 1):
        return False
    if n % 2 == 0 and n != 2:
        return False
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        else:
            f += 2
    # Only odd number is possible
    return True


def generate_question_and_answer() -> Tuple[str, str]:
    number = randint(0, 99)
    question = str(number)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
