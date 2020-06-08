from typing import Optional

from config.config import TEXT
from game.player import PLAYER
from states.state import State, StateOptions


class ReorderOptions(StateOptions):
    """Enum values for reorder options"""

    TYPE = 1
    NO = 2
    REVERSE = 3
    EXIT = 4


class Reorder(State):
    """Substate for reorganizing Pokemon on team"""

    option: Optional[ReorderOptions] = None

    def __init__(self):
        super().__init__()
        while self.option != ReorderOptions.EXIT:
            print(TEXT["TEAM"]["REORDER"]["ENTRY"])
            self.option = self.check_input(ReorderOptions)
            if self.option == ReorderOptions.TYPE:
                pass
            elif self.option == ReorderOptions.NO:
                pass
            elif self.option == ReorderOptions.REVERSE:
                PLAYER.team = PLAYER.team[::-1]


class TeamOptions(StateOptions):
    """Enum values for team management options"""

    TOSSPKMN = 1
    REORDER = 2
    EXIT = 3


class Team(State):
    """Game state for player team management"""

    option: Optional[TeamOptions] = None

    def __init__(self):
        super().__init__()
        while self.option != TeamOptions.EXIT:
            print(TEXT["TEAM"]["ENTRY"])
            self.option = self.check_input(TeamOptions)
            if self.option == TeamOptions.TOSSPKMN:
                Toss()
            elif self.option == TeamOptions.REORDER:
                Reorder()
