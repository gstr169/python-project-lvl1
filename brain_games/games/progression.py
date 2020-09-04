from typing import Tuple
from random import randint

PROGRESSION_LENGTH = 10


def progression_game() -> Tuple[str, str]:
    start_element, step = randint(0, 99), randint(0, 99)
    index_missing = randint(0, PROGRESSION_LENGTH - 1)
    progression_list = [str(start_element + step * i)
                        for i in range(0, PROGRESSION_LENGTH)]
    correct_answer = progression_list[index_missing]
    progression_list[index_missing] = '...'
    return ' '.join(progression_list), correct_answer


progression_game.welcome_message = 'What number is missing in the progression?'
