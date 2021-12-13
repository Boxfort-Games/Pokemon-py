import random
from typing import Optional

from game.typechart import Element


class Pokemon:
    """Holds information about a Pokemon's current instance"""

    name: str
    dex_number: int
    types: list[Element]
    health: int
    total_health: int

    def __init__(
        self,
        name: str,
        dex_number: int,
        types: list[Element],
        total_health: Optional[int] = None,
    ):
        self.name = name
        self.dex_number = dex_number
        self.types = types
        self.total_health = (
            total_health if total_health is not None else random.randint(20, 50)
        )
        self.health = self.total_health

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        """Converts Pokemon stats to terminal output string"""
        types_str = "".join("{:^9}".format(type) for type in self.types)
        return "#{:<3d} {:^11.11} {:2d}/{:2d}  {:18}".format(
            self.dex_number, self.name, self.health, self.total_health, types_str
        )
