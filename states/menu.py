from typing import Optional
from config.text import TEXT
from getkey import getkey
from states import state
from game.game import Game


class MenuOptions(state.StateOptions):
    BATTLE = 1
    TEAM = 2
    EXIT = 3


class Menu(state.State):
    option: Optional[MenuOptions] = None

    def __init__(self, game: Game):
        super().__init__(game)
        self.check_input()

    def check_input(self):
        while self.option is not MenuOptions.EXIT:
            print(TEXT["MAIN"]["ENTRY"])
            print(*self.list_options(MenuOptions), sep='\n')
            print(TEXT["MISC"]["PROMPT"])
            try:
                choice = int(getkey())
                self.option = MenuOptions(choice)
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
            except ValueError:
                print(TEXT["MISC"]["ERROR"])
