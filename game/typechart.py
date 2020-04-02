from enum import Enum, auto


class Element(Enum):
    """Possible types that Pokemon can be"""

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

    def __repr__(self) -> str:
        return self.name.capitalize()


class Multiplier(Enum):
    """Type advantage calculations"""

    STRONG = 2
    NORMAL = 1
    WEAK = 0.5
    NO_EFFECT = 0


TYPECHART = {
    Element.NORMAL: {
        Element.ROCK: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.GHOST: Multiplier.NO_EFFECT,
    },
    Element.FIRE: {
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.ICE: Multiplier.STRONG,
        Element.BUG: Multiplier.STRONG,
        Element.ROCK: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
    },
}
