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
    ineffect ive: List[Element]
    immune: List[Element]

    def __init__(
        self,
        element: Element,
        strong: List[Element] = None,
        ineffective: List[Element] = None,
        immune: List[Element] = None
    ):
        self.element = element
        if strong is not None:
            self.strong = strong
        if ineffective is not None:
            self.ineffective = ineffective
        if immune is not None:
            self.immune = immune


class Pokemon():
    name: str
    type: List[Types] = []
    number: int
    health: int

    def __init__(self, name: str, type: Union[Types, List[Types]], number: int, health: int = random.randint(20, 50)):
        self.name = name
        self.number = number
        self.health = health
        if isinstance(type, Types):
            self.type.append(type)
        else:
            self.type = type
