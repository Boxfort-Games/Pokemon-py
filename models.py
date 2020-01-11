from enum import Enum, auto
from typing import Type


class Types(Enum):
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


class Pokemon():
    name: str
    type: Types
    number: int

    def __init__(self, name: str, type: Types, number: int):
        self.name = name
        self.type = type
        self.number = number
