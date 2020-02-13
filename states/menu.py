from typing import Optional

from config.config import TEXT
from states.state import State, StateOptions


class MenuOptions(StateOptions):
    BATTLE = 1
    TEAM = 2
    EXIT = 3


class Menu(State):
    option: Optional[MenuOptions] = None

    def __init__(self):
        super().__init__()
        while self.option is not MenuOptions.EXIT:
            print(TEXT["MAIN"]["ENTRY"])
            self.option = self.check_input(MenuOptions)
            self.choose_option()

    def choose_option(self):
        if self.option == MenuOptions.BATTLE:
            # Enter battle
            print("battle")
            pass
        elif self.option == MenuOptions.TEAM:
            # Enter team
            print("team")
            pass
        elif self.option == MenuOptions.EXIT:
            # Exit
            print(TEXT["MAIN"]["EXIT"])
