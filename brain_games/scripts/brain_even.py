from brain_games.cli import welcome_user
from brain_games.even import game_flow


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')
    name = welcome_user()
    result = game_flow()
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
