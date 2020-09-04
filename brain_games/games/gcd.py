from typing import Tuple
from random import randint
from math import gcd


def gcd_game() -> Tuple[str, str]:
    number_a, number_b = randint(0, 99), randint(0, 99)
    correct_answer = gcd(number_a, number_b)
    return f'{number_a} {number_b}', str(correct_answer)


gcd_game.welcome_message = 'Find the greatest common divisor of given numbers.'
