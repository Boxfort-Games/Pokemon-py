from enum import Enum, auto
from typing import Dict, Set, Union
import random


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


class Types():
    element: Element
    effectiveness: Dict[Element, Multiplier]

    def __init__(
        self,
        element: Element,
        effectiveness: Dict[Element, Multiplier]
    ):
        self.element = element
        self.effectiveness = effectiveness


class Pokemon():
    name: str
    types: Set[Types]
    number: int
    health: int

    def __init__(self, name: str, types: Union[Types, Set[Types]], number: int, health: int = random.randint(20, 50)):
        self.name = name
        self.number = number
        self.health = health
        if isinstance(types, Types):
            self.types = {types}
        else:
            self.types = types
