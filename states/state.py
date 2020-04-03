from enum import IntEnum
from typing import List, Type, TypeVar

from readchar import readkey

from config.config import TEXT

T = TypeVar("T")


class StateOptions(IntEnum):
    """Gives Menu Option values"""

    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"

    @classmethod
    def list_options(cls: Type[T]) -> List[str]:
        """Returns the the options as a string for application to print to user"""

        return [repr(option) for option in cls]


class State:
    """Base class for game states"""

    @staticmethod
    def check_input(option_type: Type[T]) -> T:
        """Receives user input runs application accordingly even in the case an option not available is chosen"""
        print(*option_type.list_options(), sep="\n")
        print(TEXT["MISC"]["PROMPT"])
        try:
            choice = readkey()
            print(choice)
            return option_type(int(choice))
        except ValueError:
            print(TEXT["MISC"]["ERROR"])
