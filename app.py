from game.game import Game
from states.menu import Menu


def main():
    game = Game()
    print(str(*game.team))
    Menu(game)


if __name__ == '__main__':
    main()
