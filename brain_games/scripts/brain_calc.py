from brain_games.cli import game_flow
from brain_games.games import calc_question


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?', end='\n\n')
    game_flow(calc_question())


if __name__ == '__main__':
    main()
