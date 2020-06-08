from typing import Optional

from readchar import readkey

from config.config import TEXT
from game.player import PLAYER
from states.state import State, StateOptions


class Toss(State):
    """Substate for tossing Pokemon from team"""

    is_tossing: bool = True

    def __init__(self):
        super().__init__()
        while self.is_tossing:
            if len(PLAYER.team) > 1:
                print(TEXT["TEAM"]["TOSS"])
                print(
                    *[f"{str(i+1)}. {slot.name}" for i, slot in enumerate(PLAYER.team)],
                    sep="\n",
                )
                print(TEXT["TEAM"]["EXIT"], end="\n" * 2)

                self.is_tossing = self.attempt_toss()
            else:
                print(TEXT["TEAM"]["SIZE_ERROR"], end="\n" * 2)
                self.is_tossing = False

    @staticmethod
    def attempt_toss() -> bool:
        """Receives user input and attempts to toss a pokemon"""
        try:
            choice = readkey()
            player_toss_choice = PLAYER.team[int(choice) - 1]
            print(
                f"{player_toss_choice.name} {TEXT['TEAM']['RESULT']} {player_toss_choice.name}!",
                end="\n" * 2,
            )
            PLAYER.team.remove(player_toss_choice)
            return False
        except IndexError:
            # Index not found in PLAYER.team
            print(TEXT["TEAM"]["ERROR"], end="\n" * 2)
            return True
        except ValueError:
            # Key other than number was pressed
            return False


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
