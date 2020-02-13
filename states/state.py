from enum import IntEnum
from typing import List, Optional, Type


class StateOptions(IntEnum):
    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"


class State:
    option: Optional[StateOptions]

    def list_options(self, option_type: Type[IntEnum]) -> List[str]:
        return list(map(lambda option: repr(option), option_type))
