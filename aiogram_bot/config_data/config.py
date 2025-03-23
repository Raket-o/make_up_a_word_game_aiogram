"""
The config module is used to check whether the environment has been created.
"""

import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = os.getenv("START_MESSAGE")
ADMINS_TELEGRAM_ID = [int(i) for i in os.getenv("ADMINS_TELEGRAM_ID").split()]
