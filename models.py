from enum import Enum, auto
from typing import List, Union
import random


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
    strong: List[Element]
    weak: List[Element]
    void: List[Element]

    def __init__(
        self,
        element: Element,
        strong: List[Element] = None,
        weak: List[Element] = None,
        void: List[Element] = None
    ):
        self.element = element
        if strong is not None:
            self.strong = strong
        if weak is not None:
            self.weak = weak
        if void is not None:
            self.void = void


class Pokemon():
    name: str
    types: List[Types]
    number: int
    health: int

    def __init__(self, name: str, types: Union[Types, List[Types]], number: int, health: int = random.randint(20, 50)):
        self.name = name
        self.number = number
        self.health = health
        if isinstance(types, Types):
            self.types = [types]
        else:
            self.types = types
