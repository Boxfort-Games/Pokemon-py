from typing import List

from api import pokeapi
from game.pokemon import Pokemon


class Player:
    team: List[Pokemon] = []

    def __init__(self):
        if (len(self.team) < 1):
            self.team.append(pokeapi.get_random_pokemon_from_api())


PLAYER = Player()
