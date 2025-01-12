"""Bot Telegram Initialization module."""

import logging
from asyncio import get_event_loop

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import BOT_TOKEN

logger = logging.getLogger(__name__)


async def start_up():
    """The start_up function. Outputs text to the console at startup."""
    logging.info("Bot started")


async def on_shutdown():
    """The on_shutdown function. Outputs text to the console at startup."""
    logging.info("Bot stopped")


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

loop = get_event_loop()
dp = Dispatcher()

