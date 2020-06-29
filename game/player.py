import asyncio
from typing import Callable, List

from readchar import readkey

from api import pokeapi
from config.config import TEXT
from game.pokemon import Pokemon


class Player:
    """Holds current information about the player"""

    team: List[Pokemon] = []

    def __init__(self):
        """Fills the player's team with a random Pokemon from the PokeAPI"""
        self.add_to_team(asyncio.run(pokeapi.get_random_pokemon_from_api()))
        self.team.extend(asyncio.run(pokeapi.get_random_pokemons_from_api(2)))

    def add_to_team(self, pokemon: Pokemon):
        """Add a pokemon to the user's team and inform the user"""
        self.team.append(pokemon)
        print(f"{pokemon.name} {TEXT['POKEMON']['ADD']}")

    def remove_from_team(self):
        """Prompts user to remove a pokemon from the user's team"""
        self.__attempt_manage(
            self.team.pop, TEXT["TEAM"]["TOSS"], TEXT["TEAM"]["RESULT_TOSS"]
        )

    def print_team(self):
        print(
            *[f"{str(i+1)}. {slot.name}" for i, slot in enumerate(self.team)], sep="\n",
        )

    def set_first(self):
        self.__attempt_manage(
            self.__move_to_start, TEXT["TEAM"]["FIRST"], TEXT["TEAM"]["RESULT_FIRST"]
        )

    def __move_to_start(self, index: int):
        first = self.team.pop(index)
        self.team.insert(0, first)

    def __attempt_manage(self, func: Callable, prompt: str, result: str):
        """Receives user input and attempts to toss a pokemon"""
        is_managing = True
        if len(self.team) <= 1:
            print(TEXT["TEAM"]["SIZE_ERROR"], end="\n" * 2)
            is_managing = False
        while is_managing:
            print(prompt)
            self.print_team()
            print(TEXT["TEAM"]["EXIT"], end="\n" * 2)
            try:
                choice = readkey()
                manage_index = int(choice) - 1
                manage_choice = self.team[manage_index]
                if manage_index < 0:
                    raise IndexError
                print(result.format(manage_choice.name, manage_choice.name), end="\n" * 2)
                func(manage_index)
                is_managing = False
            except IndexError:
                # Index not found in team
                print(TEXT["TEAM"]["EXIST_ERROR"], end="\n" * 2)
                is_managing = True
            except ValueError:
                # Key other than number was pressed
                is_managing = False

    def print_team_detail(self):
        """Prints a formatted table of the player's team"""
        header = "{:4} {:^11} {:6} {:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(*[str(pokemon) for pokemon in self.team], sep="\n", end="\n" * 2)


"""Global Player instance"""
PLAYER = Player()
