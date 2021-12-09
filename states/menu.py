from typing import Optional

from config.config import MESSAGES
from states.battle import Battle
from states.state import State, StateOptions
from states.team import Team


class MenuOptions(StateOptions):
    """Enum values for options available in the menu"""

    BATTLE = 1
    TEAM = 2
    EXIT = 3


class Menu(State):
    """Game state for main menu"""

    option: Optional[MenuOptions] = None

    def __init__(self):
        """Initializes the menu state, lists available options, and checks against user input"""
        super().__init__()
        while self.option != MenuOptions.EXIT:
            print(MESSAGES["MAIN"]["ENTRY"], end="\n" * 2)
            self.option = self.check_input(MenuOptions)
            self.choose_option()

    def choose_option(self):
        """Enters next game state based on player choice"""
        if self.option == MenuOptions.BATTLE:
            Battle()
        elif self.option == MenuOptions.TEAM:
            Team()
        elif self.option == MenuOptions.EXIT:
            # Exit
            print(MESSAGES["MAIN"]["EXIT"], end="\n" * 2)
