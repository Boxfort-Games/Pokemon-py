import typechart
from models import Pokemon


def main():
    eevee = Pokemon("Eevee", typechart.NORMAL, 133)
    # eevee: Pokemon
    # health: 41
    # name: "Eevee"
    # number: 133
    # types: List
    #     0: TypeInfo
    #         element: Element.NORMAL,
    #         effectiveness: {
    #             Element.ROCK: Multiplier.WEAK,
    #             Element.STEEL: Multiplier.WEAK,
    #             Element.GHOST: Multiplier.NO_EFFECT
    #         }


if __name__ == '__main__':
    main()
