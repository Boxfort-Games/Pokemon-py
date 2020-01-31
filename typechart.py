from models import Element, Types

NORMAL = Types(
    Element.NORMAL,
    weak=[Element.ROCK, Element.STEEL],
    void=[Element.GHOST]
)

ELECTRIC = Types(
    Element.ELECTRIC,
    [Element.FLYING, Element.WATER],
    [Element.GRASS, Element.ELECTRIC],
    [Element.GROUND]
)

FIRE = Types(
    Element.FIRE,
    [Element.BUG, Element.STEEL, Element.GRASS, Element.ICE],
    [Element.ROCK, Element.FIRE, Element.DRAGON],
)

WATER = Types(
    Element.WATER,
    [Element.GROUND, Element.ROCK, Element.FIRE],
    [Element.WATER, Element.GRASS, Element.DRAGON],
)
