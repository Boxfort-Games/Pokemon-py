import asyncio
from typing import Optional

from api import pokeapi
from config.config import TEXT
from game.pokemon import Pokemon
from states.state import State, StateOptions


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
        print(TEXT["BATTLE"]["ENTRY"].format(self.enemy.name), end="\n" * 2)
        while self.option != BattleOptions.RUN:
            self.option = self.check_input(BattleOptions)
            if self.option == BattleOptions.FIGHT:
                pass
            elif self.option == BattleOptions.TEAM:
                pass
            elif self.option == BattleOptions.CATCH:
                pass
