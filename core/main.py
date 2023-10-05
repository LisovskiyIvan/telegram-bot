import asyncio
import logging
import sys

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from utils.commands import set_commands
from handlers.commandHandler import commandRouter
from handlers.basicHandler import basicRouter

TOKEN = '6514750226:AAHIM-kQYuzB1-2SK1Hw5wjUYH3rkkol0AA'







async def main() -> None:
    
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(commandRouter, basicRouter)
    await set_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())