import pokepy
from game.pokemon import Pokemon

client = pokepy.V2Client(cache='in_disk', cache_location='/temp')


def get_random_pokemon() -> Pokemon:
    # client.get_pokemon()
    # map_pokepy_to_pokemon()
    pass


def map_pokepy_to_pokemon(pokepy_mon: any) -> Pokemon:
    pass
