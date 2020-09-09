import prompt

NUMBER_OF_QUESTIONS = 3


def welcome_message():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def welcome_user():
    welcome_message()
    get_user_name()


def game_flow(game_module) -> None:
    welcome_message()
    print(game_module.DESCRIPTION, end='\n\n')
    name = get_user_name()
    for _i in range(NUMBER_OF_QUESTIONS):
        question, correct_answer = game_module.generate_question_and_answer()
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
