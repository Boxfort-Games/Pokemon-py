from game.player import PLAYER
from states.menu import Menu


def main():
    """Entry point for the application"""
    PLAYER.print_team()
    Menu()


if __name__ == "__main__":
    main()
