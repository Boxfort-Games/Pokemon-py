from enum import IntEnum
from typing import List, Optional, Type

from game.game import Game


class StateOptions(IntEnum):
    def __repr__(self) -> str:
        return f"{self.value}: {self.name}"


class State:
    game: Game
    option: Optional[StateOptions]

    def __init__(self, game: Game):
        self.game = game

    def list_options(self, option_type: Type[IntEnum]) -> List[str]:
        return list(map(lambda option: repr(option), option_type))
