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


class Pokemon:
    def __init__(
        self,
        name: str,
        types: Union[TypeInfo, List[TypeInfo]],
        number: int,
        health: Optional[int] = None
    ):
        self.name = name
        self.number = number
        self.health = health if health is not None else random.randint(20, 50)
        self.types = [types] if isinstance(types, TypeInfo) else types
