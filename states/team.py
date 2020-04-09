from typing import Optional

from readchar import readkey

from config.config import TEXT
from game.player import PLAYER
from states.state import State, StateOptions


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
        while self.option is not TeamOptions.EXIT:
            print(TEXT["TEAM"]["ENTRY"])
            self.option = self.check_input(TeamOptions)
            self.choose_option()

    def choose_option(self):
        """Performs team action based on player choice"""
        if self.option == TeamOptions.TOSSPKMN:
            Toss()
        elif self.option == TeamOptions.REORDER:
            pass


class Toss(State):
    """Substate for tossing Pokemon from team"""

    def __init__(self):
        super().__init__()
        if len(PLAYER.team) > 1:
            # Print prompt
            # Print list of pokemon with numbers
            choice = readkey()
            # Toss pokemon of choice


class ReorderOptions(StateOptions):
    """Enum values for reorder options"""

    TYPE = 1
    NO = 2
    REVERSE = 3


class Reorder(State):
    """Substate for reorganizing Pokemon on team"""

    option: Optional[ReorderOptions] = None

    def __init__(self):
        super().__init__()
