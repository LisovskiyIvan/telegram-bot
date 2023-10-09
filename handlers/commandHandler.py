from aiogram import Router, F
from aiogram.types import Message
from keys.reply import reply_keyboard, go_back_kb


commandRouter = Router()

@commandRouter.message(F.text == '/start')
async def get_start(message: Message):
    await message.answer("Старт", reply_markup=reply_keyboard)

@commandRouter.message(F.text == '/help')
async def get_help(message: Message):
    await message.answer('Эта первая версия бота(1.0v). В будущем он будет дорабатываться. Я знаю что бот работает довольно медленно и уже работаю над этим.\nПрошу не спамить кнопки для корректной работы бота.\nРеализован с помощью jikan api. По всем вопросам и предложениям обращаться к создателю @daymewannabe', reply_markup=go_back_kb)


