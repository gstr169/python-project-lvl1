import prompt
from random import randint


def progression_question() -> tuple:
    element, step = randint(0, 99), randint(0, 99)
    index_missing = randint(0, 9)
    correct_answer = 0
    print('Question: ')
    for i in range(0, 10):
        if i == index_missing:
            correct_answer = element
            print('..', end=' ')
        else:
            print(element, end=' ')
        element += step
    print('\n')
    answer = prompt.string('Your answer: ')
    if answer == str(correct_answer):
        return True, correct_answer, answer
    else:
        return False, correct_answer, answer
