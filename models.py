import random
from enum import Enum, auto
from typing import Dict, List, NamedTuple, Optional, Union


class Multiplier(Enum):
    STRONG = 2
    NORMAL = 1
    WEAK = 0.5
    NO_EFFECT = 0


class Element(Enum):
    NORMAL = auto()
    FIGHT = auto()
    FLYING = auto()
    POISON = auto()
    GROUND = auto()
    ROCK = auto()
    BUG = auto()
    GHOST = auto()
    STEEL = auto()
    FIRE = auto()
    WATER = auto()
    GRASS = auto()
    ELECTRIC = auto()
    PSYCHIC = auto()
    ICE = auto()
    DRAGON = auto()
    DARK = auto()
    FAIRY = auto()


class TypeInfo(NamedTuple):
    element: Element
    effectiveness: Dict[Element, Multiplier]

    def __repr__(self) -> str:
        return self.element.name.capitalize()


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

    def __repr__(self) -> str:
        return f"""
            Pokemon #{self.dex_number}
            ==================
            Name: {self.name}
            Type: {str(self.types)[1:-1]}
            Health: {self.health}/{self.total_health}
        """
