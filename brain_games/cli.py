import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_flow(question_def) -> None:
    name = welcome_user()
    for _i in range(0, 3):
        result, correct, answer = question_def()
        if result:
            print('Correct!')
        else:
            print(f"""
                '{answer}' is wrong answer ;(. 
                Correct answer was '{correct}'.
            """)
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
