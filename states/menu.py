from enum import Enum
from typing import Optional, List
from config.text import TEXT
from getkey import getkey


class MenuStates(Enum):
    BATTLE = 1
    TEAM = 2
    EXIT = 3

    def __repr__(self) -> str:
        return f"{self.value}: {self.name}"


class Menu:
    state: Optional[MenuStates] = None

    def __init__(self):
        self.check_input()

    def list_options(self) -> List[str]:
        # Rewrite with map lambda
        options: List[str] = []
        for option in MenuStates:
            options.append(repr(option))
        return options

    def check_input(self):
        print(TEXT["MAIN"]["ENTRY"])
        while self.state is not MenuStates.EXIT:
            self.list_options()
            print(TEXT["MISC"]["PROMPT"])
            try:
                choice = int(getkey())
                Menu.state = MenuStates(choice)
                if Menu.state == MenuStates.BATTLE:
                    # Enter battle
                    pass
                elif Menu.state == MenuStates.TEAM:
                    # Enter team
                    pass
                elif Menu.state == MenuStates.EXIT:
                    # Exit
                    print(TEXT["MAIN"]["EXIT"])
            except ValueError:
                print(TEXT["MISC"]["ERROR"])
