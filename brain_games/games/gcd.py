import prompt
from random import randint
from math import gcd


def gcd_question() -> tuple:
    number_a, number_b = randint(0, 99), randint(0, 99)
    correct_answer = gcd(number_a, number_b)
    print(f'Question: {number_a} {number_b}')
    answer = prompt.string('Your answer: ')
    if answer == str(correct_answer):
        return True, correct_answer, answer
    else:
        return False, correct_answer, answer
