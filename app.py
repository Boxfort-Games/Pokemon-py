from states.menu import Menu
from game.game import Game


def main():
    game = Game()
    print(str(*game.team))
    Menu(game)


if __name__ == '__main__':
    main()
