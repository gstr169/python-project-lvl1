from brain_games.cli import game_flow
from brain_games.games import even_question


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')
    game_flow(even_question)


if __name__ == '__main__':
    main()
