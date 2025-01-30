"""The command module /start."""

import logging

from aiogram import types
from aiogram.fsm.context import FSMContext

from config_data.config import START_MESSAGE
from states.states import DialogueUserState
from utils.make_word import find_words

start_logger = logging.getLogger(__name__)


async def start_command_1(message: types.Message, state: FSMContext = None) -> None:
    """
    Output of the START_MESSAGE and waiting for user input.
    """
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name

    await message.answer(START_MESSAGE, parse_mode="HTML")
    start_logger.info(f"start_logger-UserID={telegram_id} {full_name}")

    await state.set_state(DialogueUserState.input_word)


async def start_command_2(message: types.Message, state: FSMContext) -> None:
    """
    Outputs words to the user using the specified characters.
    """
    dict_words: dict[int:list[str]] = await find_words(message.text.lower())
    if dict_words:
        for count_letter, words in dict_words.items():
            await message.answer(f"Слова из {count_letter} букв: {', '.join(words)}")
    else:
        await message.answer("Что-то слишком тяжело, давай попробуем другие буквы")

    await start_command_1(message, state)
