import prompt
from random import randint

ANSWERS = {
    'no': False,
    'yes': True,
}


def ask_question() -> tuple:
    number = randint(0, 99)
    correct_answer = (number % 2) == 0
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if ANSWERS.get(answer) == correct_answer:
        return True, correct_answer, answer
    else:
        return False, correct_answer, answer


def game_flow() -> bool:
    for i in range(0, 3):
        result, correct_answer, answer = ask_question()
        if result:
            print('Correct!')
        else:
            correct = list(ANSWERS)[correct_answer]
            print(f"''{answer}'' is wrong answer ;(. Correct answer was '{correct}'.")
            print("Let's try again, Bill!")
            return False
    return True
