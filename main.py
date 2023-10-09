import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from utils.commands import set_commands
from handlers.commandHandler import commandRouter
from handlers.basicHandler import basicRouter
from utils.config import TOKEN

  
async def main() -> None:
    
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(commandRouter, basicRouter)
    await set_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())