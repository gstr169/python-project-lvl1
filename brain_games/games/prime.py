import prompt
from random import randint
from brain_games.constants import ANSWERS


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


def prime_question() -> tuple:
    number = randint(0, 99)
    correct_answer = is_prime(number)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if ANSWERS.get(answer) == correct_answer:
        return True, list(ANSWERS)[correct_answer], answer
    else:
        return False, list(ANSWERS)[correct_answer], answer
