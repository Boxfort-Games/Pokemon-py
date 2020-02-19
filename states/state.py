from enum import IntEnum
from typing import List, Type, TypeVar

from readchar import readkey

from config.config import TEXT


T = TypeVar('T')


class StateOptions(IntEnum):
    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"

    @classmethod
    def list_options(cls: Type[T]) -> List[str]:
        return list(map(lambda option: repr(option), cls))


class State:
    @staticmethod
    def check_input(option_type: Type[T]) -> T:
        print(*option_type.list_options(), sep="\n")
        print(TEXT["MISC"]["PROMPT"])
        try:
            choice = readkey()
            print(choice)
            return option_type(int(choice))
        except ValueError:
            print(TEXT["MISC"]["ERROR"])
