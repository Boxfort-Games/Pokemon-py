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

    def __init__(self):
        super().__init__()
        self.enemy = asyncio.run(pokeapi.get_random_pokemon_from_api())
        is_escape = False
        print(MESSAGES["BATTLE"]["ENTRY"].format(self.enemy.name), end="\n" * 2)
        print(f"Go {PLAYER.lead_pokemon.name}! \n")
        while is_escape is not True:
            self.option = self.check_input(BattleOptions)
            # TODO: Implement battling
            if self.option == BattleOptions.FIGHT:
                pass
            elif self.option == BattleOptions.TEAM:
                pass
            elif self.option == BattleOptions.CATCH:
                pass
            elif self.option == BattleOptions.RUN:
                is_escape = self.calc_run_prob()

    def calc_run_prob(self) -> bool:
        """Calculates run failure as a percentage of enemy health to player health and caps it at 90%"""

        run_calc = min(self.enemy.health / PLAYER.lead_pokemon.health, 0.9)
        run_chance = random.random()
        if run_chance > run_calc:
            print("Got away safely! \n")
            return True
        else:
            print("Failed to run!")
            print(f"Wild {self.enemy.name} attacked! \n")
            return False
