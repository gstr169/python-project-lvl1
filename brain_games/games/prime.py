from typing import Tuple
from random import randint

ANSWERS = {
    'no': False,
    'yes': True,
}


def is_prime(n: int) -> bool:
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


def prime_game() -> Tuple[str, str]:
    number = randint(0, 99)
    correct_answer = is_prime(number)
    return str(number), list(ANSWERS)[correct_answer]


prime_game.welcome_message = 'Answer "yes" if given number is prime. ' \
                             'Otherwise answer "no".'
