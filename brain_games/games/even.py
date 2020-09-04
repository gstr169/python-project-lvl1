from typing import Tuple
from random import randint

ANSWERS = {
    'no': False,
    'yes': True,
}


def even_game() -> Tuple[str, str]:
    number = randint(0, 99)
    correct_answer = (number % 2) == 0
    return str(number), list(ANSWERS)[correct_answer]


even_game.welcome_message = 'Answer "yes" if number even ' \
                            'otherwise answer "no".'
