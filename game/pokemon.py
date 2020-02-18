import random
from textwrap import dedent
from typing import List, Optional, Union

from game.typechart import TypeInfo


class Pokemon:
    name: str
    dex_number: int
    types: List[TypeInfo]
    health: int
    total_health: int

    def __init__(
        self,
        name: str,
        dex_number: int,
        types: Union[TypeInfo, List[TypeInfo]],
        total_health: Optional[int] = None
    ):
        self.name = name
        self.dex_number = dex_number
        self.types = [types] if isinstance(types, TypeInfo) else types
        self.total_health = total_health if total_health is not None else random.randint(
            20, 50)
        self.health = self.total_health

    def __str__(self) -> str:
        return dedent(
            f"""
            Pokemon #{self.dex_number}
            Name: {self.name}
            Type: {str(self.types)[1:-1]}
            Health: {self.health}/{self.total_health}
            """
        )
