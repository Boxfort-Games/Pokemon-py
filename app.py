from game.player import PLAYER
from config.config import TEXT
from states.menu import Menu


def main():
    """Entry point for the application"""

    init_player()
    Menu()


def init_player():
    """Start PLAYER instance and inform the player of their first Pokemon"""

    print(f"{PLAYER.team[0].name} {TEXT['POKEMON']['ADD']}")
    PLAYER.print_team()


if __name__ == "__main__":
    main()
