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

    def print_team(self):
        """Neatly print a formatted table of the player's team"""
        header = "{:4} {:11} {:6}{:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(str(*self.team), end="\n" * 2)


"""Global Player instance"""
PLAYER = Player()
