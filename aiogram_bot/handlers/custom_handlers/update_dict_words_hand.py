"""Dictionary Update Module."""

import logging

from aiogram import types
from aiogram.fsm.context import FSMContext

from handlers.default_heandlers.start import start_command_1
from utils.make_word import find_words_obj


update_dict_logger = logging.getLogger(__name__)


async def update_dict(
    message: [types.CallbackQuery, types.Message], state: FSMContext
) -> None:
    """
    The update_dict function.
    A callback with the update_dict_words date triggers this function.
    Updates the dictionary.
    """
    find_words_obj.update_dict_words()
    update_dict_logger.info("The dictionary with words has been updated")
    await message.answer("Словарь обновлён")
    await state.clear()
    await start_command_1(message, state)
