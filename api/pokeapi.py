import random

import pokepy

from game.pokemon import Pokemon
from game.typechart import Element

client = pokepy.V2Client(cache='in_disk', cache_location='./temp')

MAX_DEX_NUMBER = 807


def get_random_pokemon_from_api() -> Pokemon:
    rand_dex_id = random.randint(1, MAX_DEX_NUMBER)
    pokepy_mon = client.get_pokemon(rand_dex_id)
    return map_pokepy_to_pokemon(pokepy_mon)


def map_pokepy_to_pokemon(pokepy_mon: any) -> Pokemon:
    type_list = [
        Element[pokepy_type.type.name.upper()]
        for pokepy_type in pokepy_mon.types
    ]
    return Pokemon(pokepy_mon.name.capitalize(), pokepy_mon.id, type_list)
