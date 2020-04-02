from game.player import PLAYER
from states.menu import Menu


def main():
    """Entry point for application"""

    print(str(*PLAYER.team))
    Menu()


if __name__ == "__main__":
    main()
