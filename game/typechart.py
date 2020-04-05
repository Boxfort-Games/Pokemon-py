from enum import Enum, auto


class Element(Enum):
    """Possible types that a Pokemon can be"""

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

    def __str__(self) -> str:
        return self.name.capitalize()


class Multiplier(Enum):
    """Enum values for possible type advantage factors"""

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
    Element.FIGHTING: {
        Element.NORMAL: Multiplier.STRONG,
        Element.FLYING: Multiplier.WEAK,
        Element.POISON: Multiplier.WEAK,
        Element.ROCK: Multiplier.STRONG,
        Element.BUG: Multiplier.WEAK,
        Element.GHOST: Multiplier.NO_EFFECT,
        Element.STEEL: Multiplier.STRONG,
        Element.PSYCHIC: Multiplier.WEAK,
        Element.ICE: Multiplier.STRONG,
        Element.DARK: Multiplier.STRONG,
        Element.FAIRY: Multiplier.WEAK,
    },
    Element.FLYING: {
        Element.FIGHTING: Multiplier.STRONG,
        Element.ROCK: Multiplier.WEAK,
        Element.BUG: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.ELECTRIC: Multiplier.WEAK,
    },
    Element.POISON: {
        Element.POISON: Multiplier.WEAK,
        Element.GROUND: Multiplier.WEAK,
        Element.ROCK: Multiplier.WEAK,
        Element.GHOST: Multiplier.WEAK,
        Element.STEEL: Multiplier.NO_EFFECT,
        Element.GRASS: Multiplier.STRONG,
        Element.FAIRY: Multiplier.STRONG,
    },
    Element.GROUND: {
        Element.FLYING: Multiplier.NO_EFFECT,
        Element.POISON: Multiplier.STRONG,
        Element.ROCK: Multiplier.STRONG,
        Element.BUG: Multiplier.WEAK,
        Element.STEEL: Multiplier.STRONG,
        Element.FIRE: Multiplier.STRONG,
        Element.GRASS: Multiplier.WEAK,
        Element.ELECTRIC: Multiplier.STRONG,
    },
    Element.ROCK: {
        Element.FIGHTING: Multiplier.WEAK,
        Element.FLYING: Multiplier.STRONG,
        Element.GROUND: Multiplier.WEAK,
        Element.BUG: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.STRONG,
        Element.ICE: Multiplier.STRONG,
    },
    Element.BUG: {
        Element.FIGHTING: Multiplier.WEAK,
        Element.FLYING: Multiplier.WEAK,
        Element.POISON: Multiplier.WEAK,
        Element.GHOST: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.PSYCHIC: Multiplier.STRONG,
        Element.DARK: Multiplier.STRONG,
        Element.FAIRY: Multiplier.WEAK,
    },
    Element.GHOST: {
        Element.NORMAL: Multiplier.NO_EFFECT,
        Element.GHOST: Multiplier.STRONG,
        Element.PSYCHIC: Multiplier.STRONG,
        Element.DARK: Multiplier.WEAK,
    },
    Element.STEEL: {
        Element.ROCK: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.WEAK,
        Element.ELECTRIC: Multiplier.WEAK,
        Element.ICE: Multiplier.STRONG,
        Element.FAIRY: Multiplier.STRONG,
    },
    Element.FIRE: {
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.ICE: Multiplier.STRONG,
        Element.BUG: Multiplier.STRONG,
        Element.ROCK: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
        Element.STEEL: Multiplier.STRONG,
    },
    Element.WATER: {
        Element.GROUND: Multiplier.STRONG,
        Element.ROCK: Multiplier.STRONG,
        Element.FIRE: Multiplier.STRONG,
        Element.WATER: Multiplier.WEAK,
        Element.GRASS: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
    },
    Element.GRASS: {
        Element.FLYING: Multiplier.WEAK,
        Element.POISON: Multiplier.WEAK,
        Element.GROUND: Multiplier.STRONG,
        Element.ROCK: Multiplier.STRONG,
        Element.BUG: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.STRONG,
        Element.GRASS: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
    },
    Element.ELECTRIC: {
        Element.FLYING: Multiplier.STRONG,
        Element.GROUND: Multiplier.NO_EFFECT,
        Element.WATER: Multiplier.STRONG,
        Element.GRASS: Multiplier.WEAK,
        Element.ELECTRIC: Multiplier.WEAK,
        Element.DRAGON: Multiplier.WEAK,
    },
    Element.PSYCHIC: {
        Element.FIGHTING: Multiplier.STRONG,
        Element.POISON: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.PSYCHIC: Multiplier.WEAK,
        Element.DARK: Multiplier.NO_EFFECT,
    },
    Element.ICE: {
        Element.FLYING: Multiplier.STRONG,
        Element.GROUND: Multiplier.STRONG,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.WEAK,
        Element.WATER: Multiplier.WEAK,
        Element.GRASS: Multiplier.STRONG,
        Element.ICE: Multiplier.WEAK,
        Element.DRAGON: Multiplier.STRONG,
    },
    Element.DRAGON: {
        Element.STEEL: Multiplier.WEAK,
        Element.DRAGON: Multiplier.STRONG,
        Element.FAIRY: Multiplier.NO_EFFECT,
    },
    Element.DARK: {
        Element.FIGHTING: Multiplier.WEAK,
        Element.GHOST: Multiplier.STRONG,
        Element.PSYCHIC: Multiplier.STRONG,
        Element.DARK: Multiplier.WEAK,
        Element.FAIRY: Multiplier.WEAK,
    },
    Element.FAIRY: {
        Element.FIGHTING: Multiplier.STRONG,
        Element.POISON: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.FIRE: Multiplier.WEAK,
        Element.DRAGON: Multiplier.STRONG,
        Element.DARK: Multiplier.STRONG,
    },
}
