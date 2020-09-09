from typing import Tuple
from random import randint

PROGRESSION_LENGTH = 10

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer() -> Tuple[str, str]:
    start_element, step = randint(0, 99), randint(0, 99)
    index_missing = randint(0, PROGRESSION_LENGTH - 1)
    progression_list = [str(start_element + step * i)
                        for i in range(0, PROGRESSION_LENGTH)]
    correct_answer = progression_list[index_missing]
    progression_list[index_missing] = '...'
    question = ' '.join(progression_list)
    return question, correct_answer
