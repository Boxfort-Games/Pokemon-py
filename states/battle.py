from typing import Optional

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
        pass
