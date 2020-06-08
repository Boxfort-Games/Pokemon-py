from operator import attrgetter
from typing import Optional

from config.config import TEXT
from game.player import PLAYER
from states.state import State, StateOptions


class ReorderOptions(StateOptions):
    """Enum values for reorder options"""

    TYPE = 1
    NAME = 2
    NUMASC = 3
    NUMDESC = 4
    REVERSE = 5
    EXIT = 6


class Reorder(State):
    """Substate for reorganizing Pokemon on team"""

    option: Optional[ReorderOptions] = None

    def __init__(self):
        super().__init__()
        print(TEXT["TEAM"]["REORDER"]["ENTRY"])
        self.option = self.check_input(ReorderOptions)
        if self.option == ReorderOptions.TYPE:
            PLAYER.team.sort(key=lambda pokemon: pokemon.types[0].name)
        elif self.option == ReorderOptions.NAME:
            PLAYER.team.sort(key=attrgetter("name"))
        elif self.option == ReorderOptions.NUMASC:
            PLAYER.team.sort(key=attrgetter("dex_number"))
        elif self.option == ReorderOptions.NUMDESC:
            PLAYER.team.sort(key=attrgetter("dex_number"), reverse=True)
        elif self.option == ReorderOptions.REVERSE:
            PLAYER.team = PLAYER.team[::-1]
        PLAYER.print_team()


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
                PLAYER.remove_from_team()
            elif self.option == TeamOptions.REORDER:
                PLAYER.print_team()
                Reorder()
