import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from utils.commands import set_commands
from handlers.commandHandler import commandRouter
from handlers.basicHandler import basicRouter
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(commandRouter, basicRouter)
    await set_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())