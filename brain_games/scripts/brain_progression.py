from brain_games.cli import game_flow
from brain_games.games import progression_question


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?', end='\n\n')
    game_flow(progression_question)


if __name__ == '__main__':
    main()
