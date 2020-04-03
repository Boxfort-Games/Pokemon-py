from typing import List

from api import pokeapi
from game.pokemon import Pokemon


class Player:
    """Holds current information about the player"""

    team: List[Pokemon] = []

    def __init__(self):
        """Fills the player's team with a random Pokemon from the PokeAPI"""

        if len(self.team) < 1:
            self.team.append(pokeapi.get_random_pokemon_from_api())


"""Global Player instance"""
PLAYER = Player()
