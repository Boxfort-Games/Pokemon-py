from typing import Optional

from config.config import TEXT
from states.battle import Battle
from states.state import State, StateOptions


class TeamOptions(StateOptions):
    """Enum values for options availabe in team menu"""

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
        """Enters next game state based on player choice"""
        if self.option == TeamOptions.TOSSPKMN:
            pass
        elif self.option == TeamOptions.REORDER:
            pass
