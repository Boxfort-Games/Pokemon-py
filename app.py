from typing import List
import random

from models import Pokemon, Types
import utils


def main():
    # Lesson one, Pokemon class and print out info
    pikachu = Pokemon("Pikachu", Types.ELECTRIC, 25)
    eevee = Pokemon("Eevee", Types.NORMAL, 133)
    print(pokemon_to_str(pikachu))
    print(pokemon_to_str(eevee))

    # Lesson two, get function to return multiple random pokemon strings
    for str in get_multiple_random_pokemon_str(100):
        print(str)


def prepend_indefinite_article(str: str) -> str:
    vowels = "aeiou"
    article = "an" if str[0].lower() in vowels else "a"
    return f"{article} {str}"


def pokemon_to_str(pokemon: Pokemon) -> str:
    return (
        f"{pokemon.name} is #{pokemon.number}. "
        f"It is {prepend_indefinite_article(pokemon.type.name)} type Pokemon."
    )


def get_multiple_random_pokemon_str(random_count: int) -> List[str]:
    pokemon_list: List[Pokemon] = [
        Pokemon("Ivysaur", Types.GRASS, 2),
        Pokemon("Squirtle", Types.WATER, 7),
        Pokemon("Charizard", Types.FIRE, 6),
        Pokemon("Mewtwo", Types.PSYCHIC, 150),
        Pokemon("Greninja", Types.DARK, 658),
        Pokemon("Incineroar", Types.FIRE, 727),
        Pokemon("Jigglypuff", Types.NORMAL, 39)
    ]

    pokemon_str_list: List[str] = []
    for i in range(utils.clamp(1, len(pokemon_list) - 1, random_count)):
        pokemon_to_add = pokemon_list[random.randint(0, len(pokemon_list) - 1)]
        pokemon_str_list.append(
            pokemon_to_str(pokemon_to_add)
        )
        pokemon_list.remove(pokemon_to_add)
    return pokemon_str_list


if __name__ == '__main__':
    main()
