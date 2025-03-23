"""The keyboard creation module."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def upd_dict_words_buttons() -> InlineKeyboardMarkup:
    """
    The function of creating a keyboard to update the dictionary with words.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="обновить словарь", callback_data="update_dict_words")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
