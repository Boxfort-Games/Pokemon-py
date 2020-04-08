from typing import Optional

from game.pokemon import Pokemon
from states.state import State, StateOptions


class BattleOptions(StateOptions):
    """Enum values for battle actions"""

    pass


class Battle(State):
    """Game state for Pokemon battle"""

    option: Optional[BattleOptions] = None
    enemy: Pokemon

    def __init__(self):
        pass
