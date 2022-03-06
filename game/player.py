import asyncio
from tabnanny import check
from xmlrpc.client import boolean

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
        self.lead_pokemon = self.team[0]
        # self.team.extend(asyncio.run(pokeapi.get_random_pokemons_from_api(2)))

    def add_to_team(self, pokemon: Pokemon):
        """Add a Pokemon to the user's team and inform the user"""
        self.team.append(pokemon)
        return f"{pokemon.name} {MESSAGES['POKEMON']['ADD']}"

    def remove_from_team(self):
        """Prompts user to remove a Pokemon from the user's team"""
        is_tossing = True
        while is_tossing:
            if len(self.team) <= 1:
                print(MESSAGES["TEAM"]["SIZE_ERROR"], end="\n" * 2)
                is_tossing = False
            else:
                print(MESSAGES["TEAM"]["TOSS"])
                print(
                    *[f"{str(i+1)}. {slot.name}" for i, slot in enumerate(self.team)],
                    sep="\n",
                )
                print(MESSAGES["TEAM"]["EXIT"], end="\n" * 2)

                is_tossing = self.__attempt_toss()

    def __attempt_toss(self) -> bool:
        """Receives user input and attempts to toss a Pokemon"""
        try:
            choice = readkey()
            player_toss_index = int(choice) - 1
            player_toss_choice = self.team[player_toss_index]

            if player_toss_index < 0:
                raise IndexError
            print(
                f"{player_toss_choice.name} {MESSAGES['TEAM']['RESULT']} {player_toss_choice.name}!",
                end="\n" * 2,
            )
            self.team.pop(player_toss_index)
            return False
        except IndexError:
            # Index not found in team
            print(MESSAGES["TEAM"]["EXIST_ERROR"], end="\n" * 2)
            return True
        except ValueError:
            # Key other than number was pressed
            if self.get_team_size() > 6:
                return False
            print(MESSAGES["TEAM"]["MUST_RELEASE"], end="\n" * 2)
            return True

    def print_team(self):
        """Prints a formatted table of the player's team"""
        header = "{:4} {:^11} {:6} {:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(*[str(pokemon) for pokemon in self.team], sep="\n", end="\n" * 2)

    def set_lead_pokemon(self):
        """Sets the team leader"""
        self.lead_pokemon = self.team[0]

    def get_team_size(self) -> int:
        """Getter for Team Size"""
        return len(self.team)

    def fainted_remove(self):
        """Removes fainted pokemon from team"""
        self.team.pop(self.team.index(self.lead_pokemon))


"""Global Player instance"""
PLAYER = Player()
