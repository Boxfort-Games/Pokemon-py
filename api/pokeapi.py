import random
from typing import List

import pokepy

from game import typechart
from game.pokemon import Pokemon

client = pokepy.V2Client(cache='in_disk', cache_location='./temp')

MAX_DEX_NUMBER = 807


def get_random_pokemon_from_api() -> Pokemon:
    rand_dex_id = random.randint(1, MAX_DEX_NUMBER)
    pokepy_mon = client.get_pokemon(rand_dex_id)
    return map_pokepy_to_pokemon(pokepy_mon)


def map_pokepy_to_pokemon(pokepy_mon: any) -> Pokemon:
    type_list: List[typechart.TypeInfo] = []
    for pokepy_type in pokepy_mon.types:
        type_name = pokepy_type.type.name.upper()
        type_info: typechart.TypeInfo = getattr(typechart, type_name)
        type_list.append(type_info)
    return Pokemon(pokepy_mon.name.capitalize(), pokepy_mon.id, type_list)
