import asyncio

from api import pokeapi
from config import MESSAGES
from readchar import readkey

from game.pokemon import Pokemon


class Player:
    """Holds current information about the player"""

    team: list[Pokemon] = []
    lead_pokemon: Pokemon

    def __init__(self):
        """Fills the player's team with a random Pokemon from the PokeAPI"""
        print(self.add_to_team(asyncio.run(pokeapi.get_random_pokemon_from_api())))
        # self.team.extend(asyncio.run(pokeapi.get_random_pokemons_from_api(5)))
        self.lead_pokemon = self.team[0]

    def add_to_team(self, pokemon: Pokemon) -> str:
        """Add a Pokemon to the user's team and inform the user"""
        self.team.append(pokemon)
        return f"{pokemon.name} {MESSAGES['POKEMON']['ADD']}"

    def remove_from_team(self):
        """Prompts user to remove a Pokemon from the user's team"""
        is_releasing = True
        while is_releasing:
            if len(self.team) < 2:
                print(MESSAGES["TEAM"]["SIZE_ERROR"], end="\n" * 2)
                is_releasing = False
            else:
                print(MESSAGES["TEAM"]["RELEASE"])
                print(
                    *[f"{str(i+1)}. {slot.name}" for i, slot in enumerate(self.team)],
                    sep="\n",
                )
                print(MESSAGES["TEAM"]["EXIT"], end="\n" * 2)

                is_releasing = self.__attempt_release()
        self.set_lead_pokemon()

    def __attempt_release(self) -> bool:
        """Receives user input and attempts to release a Pokemon"""
        try:
            choice = readkey()
            player_release_index = int(choice) - 1
            player_release_choice = self.team[player_release_index]

            if player_release_index < 0:
                raise IndexError
            print(
                f"{player_release_choice.name} {MESSAGES['TEAM']['RESULT']} {player_release_choice.name}!",
                end="\n" * 2,
            )
            self.team.pop(player_release_index)
            return False
        except IndexError:
            # Index not found in team
            print(MESSAGES["TEAM"]["EXIST_ERROR"], end="\n" * 2)
            return True
        except ValueError:
            # Key other than number was pressed
            if len(self.team) > 6:
                print(MESSAGES["TEAM"]["MUST_RELEASE"], end="\n" * 2)
                return True
            return False

    def print_team(self):
        """Prints a formatted table of the player's team"""
        header = "{:4} {:^11} {:6} {:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(*[str(pokemon) for pokemon in self.team], sep="\n", end="\n" * 2)

    def set_lead_pokemon(self, pokemon=None):
        """Sets the team leader"""
        if pokemon is not None:
            self.team[self.team.index(pokemon)] = self.lead_pokemon
            self.team[0] = pokemon
        self.lead_pokemon = self.team[0]

    def fainted_remove(self):
        """Removes fainted pokemon from team"""
        self.team.pop(self.team.index(self.lead_pokemon))
        self.set_lead_pokemon()


"""Global Player instance"""
PLAYER = Player()
