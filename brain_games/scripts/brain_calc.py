from brain_games.cli import game_flow
from brain_games.games import calc_game


def main():
    game_flow(calc_game)


if __name__ == '__main__':
    main()
