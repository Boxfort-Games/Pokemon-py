import asyncio
from typing import List

from readchar import readkey

from api import pokeapi
from config.config import TEXT
from game.pokemon import Pokemon


class Player:
    """Holds current information about the player"""

    team: List[Pokemon] = []

    def __init__(self):
        """Fills the player's team with a random Pokemon from the PokeAPI"""
        if len(self.team) < 1:
            self.team.extend(asyncio.run(pokeapi.get_random_pokemon_from_api()))

    def add_to_team(self, pokemon: Pokemon):
        """Add a pokemon to the user's team and inform the user"""
        self.team.append(pokemon)
        print(f"{pokemon.name} {TEXT['POKEMON']['ADD']}")

    def remove_from_team(self):
        is_tossing = True
        while is_tossing:
            if len(PLAYER.team) <= 1:
                print(TEXT["TEAM"]["SIZE_ERROR"], end="\n" * 2)
                self.is_tossing = False
            else:
                print(TEXT["TEAM"]["TOSS"])
                print(
                    *[f"{str(i+1)}. {slot.name}" for i, slot in enumerate(PLAYER.team)],
                    sep="\n",
                )
                print(TEXT["TEAM"]["EXIT"], end="\n" * 2)

                self.is_tossing = self.__attempt_toss()

    def __attempt_toss(self) -> bool:
        """Receives user input and attempts to toss a pokemon"""
        try:
            choice = readkey()
            player_toss_choice = self.team[int(choice) - 1]
            print(
                f"{player_toss_choice.name} {TEXT['TEAM']['RESULT']} {player_toss_choice.name}!",
                end="\n" * 2,
            )
            self.team.remove(player_toss_choice)
            return False
        except IndexError:
            # Index not found in team
            print(TEXT["TEAM"]["ERROR"], end="\n" * 2)
            return True
        except ValueError:
            # Key other than number was pressed
            return False

    def print_team(self):
        """Prints a formatted table of the player's team"""
        header = "{:4} {:^11} {:6} {:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(*[str(pokemon) for pokemon in self.team], sep="\n", end="\n" * 2)


"""Global Player instance"""
PLAYER = Player()
