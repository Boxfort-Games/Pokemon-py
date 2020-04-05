from game.player import PLAYER
from states.menu import Menu


def main():
    """Entry point for the application"""
    init_player()
    Menu()


def init_player():
    """Starts PLAYER instance and inform user of their first Pokemon"""
    PLAYER.print_team()


if __name__ == "__main__":
    main()
