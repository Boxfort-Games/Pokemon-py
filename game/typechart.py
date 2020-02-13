from game.pokemon import Element, Multiplier, TypeInfo

NORMAL = TypeInfo(
    Element.NORMAL,
    {
        Element.ROCK: Multiplier.WEAK,
        Element.STEEL: Multiplier.WEAK,
        Element.GHOST: Multiplier.NO_EFFECT
    }
)
