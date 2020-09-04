import prompt


def welcome_user(welcome_message=''):
    print('Welcome to the Brain Games!')
    print(welcome_message, end='\n\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_flow(game_def) -> None:
    name = welcome_user(game_def.welcome_message)
    for _i in range(0, 3):
        question, correct_answer = game_def()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
