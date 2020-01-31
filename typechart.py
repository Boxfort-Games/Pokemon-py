from models import Element, Types, Multiplier

NORMAL = Types(
    Element.NORMAL,
    {
        Element.ROCK: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.GHOST: Multiplier.NO_EFFECT
    }
)
