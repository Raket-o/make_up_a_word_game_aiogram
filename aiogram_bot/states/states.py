"""User data storage module (states)."""

from aiogram.fsm.state import State, StatesGroup


class DialogueUserState(StatesGroup):
    """Class DialogueUserState. Stores information and data entered by the user."""

    input_word = State()
