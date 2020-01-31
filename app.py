from models import Pokemon
import typechart


def main():
    # Lesson one, Pokemon class and print out info
    pikachu = Pokemon("Pikachu", typechart.ELECTRIC, 25)
    eevee = Pokemon("Eevee", [typechart.NORMAL, typechart.FIRE], 133)
    # print(pokemon_to_str(pikachu))
    # print(pokemon_to_str(eevee))


def prepend_indefinite_article(str: str) -> str:
    vowels = "aeiou"
    article = "an" if str[0].lower() in vowels else "a"
    return f"{article} {str}"


# def pokemon_to_str(pokemon: Pokemon) -> str:
#     return (
#         f"{pokemon.name} is #{pokemon.number}. "
#         f"It is {prepend_indefinite_article(pokemon.type.name)} type Pokemon."
#     )


# def get_multiple_random_pokemon_str(random_count: int) -> List[str]:
#     pokemon_list: List[Pokemon] = [
#         Pokemon("Ivysaur", BaseTypes.GRASS, 2),
#         Pokemon("Squirtle", BaseTypes.WATER, 7),
#         Pokemon("Charizard", BaseTypes.FIRE, 6),
#         Pokemon("Mewtwo", BaseTypes.PSYCHIC, 150),
#         Pokemon("Greninja", BaseTypes.DARK, 658),
#         Pokemon("Incineroar", BaseTypes.FIRE, 727),
#         Pokemon("Jigglypuff", BaseTypes.NORMAL, 39)
#     ]

#     pokemon_str_list: List[str] = []
#     for i in range(utils.clamp(1, len(pokemon_list) - 1, random_count)):
#         pokemon_to_add = pokemon_list[random.randint(0, len(pokemon_list) - 1)]
#         pokemon_str_list.append(
#             pokemon_to_str(pokemon_to_add)
#         )
#         pokemon_list.remove(pokemon_to_add)
#     return pokemon_str_list


if __name__ == '__main__':
    main()
