import asyncio
import random
from typing import Optional

from api import pokeapi
from config import MESSAGES
from game.player import PLAYER
from game.pokemon import Pokemon

from states import State, StateOptions


class BattleOptions(StateOptions):
    """Enum values for battle actions"""

    FIGHT = 1
    TEAM = 2
    CATCH = 3
    RUN = 4


class Battle(State):
    """Game state for Pokemon battle"""

    option: Optional[BattleOptions] = None
    enemy: Pokemon
    end_encounter = False

    def __init__(self):
        super().__init__()
        self.enemy = asyncio.run(pokeapi.get_random_pokemon_from_api())

        print(MESSAGES["BATTLE"]["ENTRY"].format(self.enemy.name), end="\n" * 2)
        self.send_pokemon(PLAYER.lead_pokemon)

        while self.end_encounter is not True:
            self.option = self.check_input(BattleOptions)
            # TODO: Implement battling
            if self.option == BattleOptions.FIGHT:
                pass
            elif self.option == BattleOptions.TEAM:
                pass
            elif self.option == BattleOptions.CATCH:
                Catch(self)
            elif self.option == BattleOptions.RUN:
                if self.calc_run_prob():
                    self.end_encounter = True
                else:
                    self.enemy_pokemon_attack()

    def calc_run_prob(self) -> bool:
        """Calculates run failure as a percentage of enemy health to player health and caps it at 90%"""

        run_calc = min(self.enemy.health / PLAYER.lead_pokemon.health, 0.9)
        run_chance = random.random()
        if run_chance > run_calc:
            print(MESSAGES["BATTLE"]["RUN_SUCESS"], end="\n" * 2)
            return True
        else:
            print(MESSAGES["BATTLE"]["RUN_FAIL"], end=" ")
            print(f"Wild {self.enemy.name} attacked!")
            return False

    def enemy_pokemon_attack(self):
        """Will handle the enemy Pokemon's attack"""
        attack = "Bite"
        attack_damage = 2
        PLAYER.lead_pokemon.health = max(PLAYER.lead_pokemon.health - attack_damage, 0)

        print(
            MESSAGES["BATTLE"]["ENEMY_ATTACK"].format(
                self.enemy.name, attack, PLAYER.lead_pokemon.name, attack_damage
            ),
            end="\n" * 2,
        )
        self.print_health(PLAYER.lead_pokemon)
        if self.check_health_zero(PLAYER.lead_pokemon) is True:
            self.health_case(PLAYER.lead_pokemon)

    def print_health(self, pokemon: Pokemon):
        """Print's the Pokemon's current and max health"""
        print(
            MESSAGES["BATTLE"]["HEALTH"].format(
                pokemon.name, pokemon.health, pokemon.total_health
            ),
            end="\n" * 2,
        )

    def check_health_zero(self, pokemon: Pokemon) -> bool:
        """Checks if Pokemon's health is less than or equal to zero"""
        if pokemon.health <= 0:
            return True
        return False

    def health_case(self, pokemon: Pokemon):
        """Handles the cases for when a Pokemon's health reaches zero"""
        self.fainted_text(pokemon)
        if len(PLAYER.team) - 1 < 1:
            print(MESSAGES["BATTLE"]["GAME_OVER"])
            quit()
        PLAYER.fainted_remove()
        pokemon = PLAYER.lead_pokemon
        self.send_pokemon(pokemon)

    def fainted_text(self, pokemon: Pokemon):
        """Prints text of Pokemon that fainted"""
        print(
            MESSAGES["BATTLE"]["FAINTED"].format(pokemon.name, pokemon.name),
            end="\n" * 2,
        )

    def send_pokemon(self, pokemon: Pokemon):
        """Prints text of the Pokemon being sent into battle"""
        print(
            MESSAGES["BATTLE"]["SEND_LEADER"].format(pokemon.name),
            end="\n" * 2,
        )
        self.print_health(pokemon)


class Catch(State):
    battle: Battle

    def __init__(self, battle: Battle):
        self.battle = battle
        battle.end_encounter = self.calc_catch_prob()
        if self.battle.end_encounter:
            self.catch_pokemon()
        else:
            self.catch_fail()

    def calc_catch_prob(self) -> bool:
        """Calculates catch failure as a percentage of enemy health to player health and caps it at 90%"""

        catch_calc = min(self.battle.enemy.health / PLAYER.lead_pokemon.health, 0.9)
        catch_chance = random.random()

        if catch_chance > catch_calc:
            return True
        else:
            return False

    def catch_pokemon(self):
        """Adds Pokemon and ensures player with a team size greater than 6 remove a Pokemon"""
        print(
            f'{MESSAGES["BATTLE"]["CATCH_SUCCESS"]} {PLAYER.add_to_team(self.battle.enemy)}',
            end="\n" * 2,
        )
        if len(PLAYER.team) > 6:
            print(MESSAGES["TEAM"]["MUST_RELEASE"], end="\n" * 2)
            PLAYER.remove_from_team()

    def catch_fail(self):
        """Handles the case for a failed catch attempt"""
        print(MESSAGES["BATTLE"]["CATCH_FAIL"].format(self.battle.enemy.name))
        self.battle.enemy_pokemon_attack()
