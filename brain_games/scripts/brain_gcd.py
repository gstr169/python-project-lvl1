from brain_games.cli import game_flow
from brain_games.games import gcd_question


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.', end='\n\n')
    game_flow(gcd_question)


if __name__ == '__main__':
    main()
