from enum import IntEnum
from typing import Type, TypeVar

from readchar import readkey

from config.config import MESSAGES

T = TypeVar("T", bound="StateOptions")


class StateOptions(IntEnum):
    """Base enum class for possible actions in game state"""

    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"

    @classmethod
    def list_options(cls: Type[T]) -> list[str]:
        """Returns the options as a list of strings for terminal output"""
        return [repr(option) for option in cls]


class State:
    """Base class for game state. Displays, holds, and reads options for state change"""

    @staticmethod
    def check_input(option_type: Type[T]):
        """Receives user input and returns corresponding StateOption"""
        print(*option_type.list_options(), sep="\n")
        print(MESSAGES["MISC"]["PROMPT"], end="\n" * 2)
        try:
            choice = readkey()
            chosen_option = option_type(int(choice))
            print(chosen_option.name, end="\n" * 2)
            return option_type(chosen_option)
        except ValueError:
            print(MESSAGES["MISC"]["OPTION_ERROR"])
