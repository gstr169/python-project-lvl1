from brain_games.cli import game_flow
from brain_games.games import prime_question


def main():
    print('Welcome to the Brain Games!')
    print(
        'Answer "yes" if given number is prime.',
        'Otherwise answer "no".', end='\n\n',
    )
    game_flow(prime_question)


if __name__ == '__main__':
    main()
