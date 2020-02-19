from enum import Enum, auto
from typing import Dict, NamedTuple


class Element(Enum):
    NORMAL = auto()
    FIRE = auto()
    WATER = auto()
    ELECTRIC = auto()
    GRASS = auto()
    ICE = auto()
    FIGHTING = auto()
    POISON = auto()
    GROUND = auto()
    FLYING = auto()
    PSYCHIC = auto()
    BUG = auto()
    ROCK = auto()
    GHOST = auto()
    DRAGON = auto()
    DARK = auto()
    STEEL = auto()
    FAIRY = auto()


class Multiplier(Enum):
    STRONG = 2
    NORMAL = 1
    WEAK = 0.5
    NO_EFFECT = 0


class TypeInfo(NamedTuple):
    element: Element
    effectiveness: Dict[Element, Multiplier]

    def __repr__(self) -> str:
        return self.element.name.capitalize()


NORMAL = TypeInfo(
    Element.NORMAL,
    {
        Element.ROCK: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.GHOST: Multiplier.NO_EFFECT
    }
)

FIRE = TypeInfo(
    Element.FIRE,
    {
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.ICE: Multiplier.STRONG,
        Element.BUG: Multiplier.STRONG,
        Element.ROCK: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK
    }
)

WATER = TypeInfo(
    Element.WATER,
    {

    }
)

ELECTRIC = TypeInfo(
    Element.ELECTRIC,
    {

    }
)

GRASS = TypeInfo(
    Element.GRASS,
    {

    }
)

ICE = TypeInfo(
    Element.ICE,
    {

    }
)

FIGHTING = TypeInfo(
    Element.FIGHTING,
    {

    }
)

POISON = TypeInfo(
    Element.POISON,
    {

    }
)

GROUND = TypeInfo(
    Element.GROUND,
    {

    }
)

FLYING = TypeInfo(
    Element.FLYING,
    {

    }
)

PSYCHIC = TypeInfo(
    Element.PSYCHIC,
    {

    }
)

BUG = TypeInfo(
    Element.BUG,
    {

    }
)

ROCK = TypeInfo(
    Element.ROCK,
    {

    }
)

GHOST = TypeInfo(
    Element.GHOST,
    {

    }
)

DRAGON = TypeInfo(
    Element.DRAGON,
    {

    }
)

DARK = TypeInfo(
    Element.DARK,
    {

    }
)

STEEL = TypeInfo(
    Element.STEEL,
    {

    }
)

FAIRY = TypeInfo(
    Element.FAIRY,
    {

    }
)
