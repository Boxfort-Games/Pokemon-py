import random
import asyncio

from aiohttp import ClientSession

from game.pokemon import Pokemon
from game.typechart import Element


"""Current highest Pokemon dex number in PokeAPI"""
MAX_DEX_NUMBER = 807

API_BASE_URL = 'https://pokeapi.co/api/v2'


async def get_pokemon_from_api(session: ClientSession, dex_id: int):
    url = f"{API_BASE_URL}/{dex_id}"
    async with session.get(url) as response:
        return await response.read()


async def get_random_pokemon_from_api(quantity: int = 1) -> None:
    """Returns a random Pokemon from the PokeAPI"""
    loop = asyncio.get_event_loop()

    tasks = []
    async with ClientSession() as session:
        for _ in range(quantity):
            rand_dex_id = random.randint(1, MAX_DEX_NUMBER)
            task = asyncio.ensure_future(get_pokemon_from_api(
                session,
                rand_dex_id
            ))
            tasks.append(task)
    results = loop.run_until_complete(asyncio.gather(*tasks))
    pass
    # return map_pokepy_to_pokemon(pokepy_mon)


def map_pokepy_to_pokemon(pokepy_mon: any) -> Pokemon:
    """Converts the data pulled from the PokeAPI and returns it as Pokemon class"""
    type_list = [
        Element[pokepy_type.type.name.upper()] for pokepy_type in pokepy_mon.types
    ]
    return Pokemon(pokepy_mon.name.capitalize(), pokepy_mon.id, type_list)
