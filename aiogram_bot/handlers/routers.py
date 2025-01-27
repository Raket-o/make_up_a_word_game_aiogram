"""User Handler registration module."""

from aiogram import F, Router
from aiogram.filters import Command, CommandStart

from handlers.default_heandlers.start import start_command_1, start_command_2
from states.states import DialogueUserState


async def register_routers(router: Router):
    """
    The register_routers function. Collects handlers in the main router.
    """
    router.message.register(start_command_1, CommandStart())
    router.callback_query.register(
        start_command_1,
        F.data.startswith("start_command=")
    )

    router.message.register(start_command_2, DialogueUserState.input_word)
