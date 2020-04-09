import asyncio
import random
from typing import Any, Awaitable, List

from aiohttp import ClientSession

from game.pokemon import Pokemon
from game.typechart import Element


"""Current highest Pokemon dex number in PokeAPI"""
MAX_DEX_NUMBER = 807

"""PokeAPI urls"""
API_BASE_URL = "https://pokeapi.co/api/v2"
API_POKEMON_URL = "/pokemon"


async def get_pokemon_from_api(session: ClientSession, dex_id: int) -> Awaitable[Any]:
    """Asynchronously fetches full Pokemon info from the API"""
    url = f"{API_BASE_URL}{API_POKEMON_URL}/{dex_id}"
    async with session.get(url) as response:
        return await response.json()


async def get_random_pokemon_from_api(quantity: int = 1) -> List[Pokemon]:
    """Asynchronously returns a number of random Pokemon from the API"""
    loop = asyncio.get_event_loop()
    tasks = []
    async with ClientSession(loop=loop) as session:
        for _ in range(quantity):
            rand_dex_id = random.randint(1, MAX_DEX_NUMBER)
            task = get_pokemon_from_api(session, rand_dex_id)
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return [map_pokepy_to_pokemon(response) for response in responses]


def map_pokepy_to_pokemon(pokepy_mon: Any) -> Pokemon:
    """Converts the data pulled from the PokeAPI and returns it as Pokemon class"""
    type_list = [
        Element[pokepy_type["type"]["name"].upper()]
        for pokepy_type in pokepy_mon["types"]
    ]
    return Pokemon(pokepy_mon["name"].capitalize(), pokepy_mon["id"], type_list)
