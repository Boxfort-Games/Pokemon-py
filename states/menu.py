from typing import Optional

from getkey import getkey

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
            self.option = self.check_input()
            self.choose_option()

    def check_input(self):
        print(TEXT["MAIN"]["ENTRY"])
        print(*self.list_options(MenuOptions), sep="\n")
        print(TEXT["MISC"]["PROMPT"])
        try:
            choice = getkey()
            print(choice)
            self.option = MenuOptions(int(choice))
        except ValueError:
            print(TEXT["MISC"]["ERROR"])

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
