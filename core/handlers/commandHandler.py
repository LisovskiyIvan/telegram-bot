from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keys.reply import reply_keyboard, random_anime_kb


commandRouter = Router()

@commandRouter.message(F.text == '/start')
async def get_start(message: Message):
    await message.answer("Старт", reply_markup=random_anime_kb)

@commandRouter.message(F.text == '/help')
async def get_help(message: Message):
    await message.answer("Простой бот, выдающий рандомные аниме и мангу. Реализован с помощью jikan api. По всем вопросам и предложениям обращаться к создателю @sexy_traktorist", reply_markup=None)

@commandRouter.message(F.text == 'Назад')
async def get_start(message: Message):
    await message.answer('',reply_markup=reply_keyboard)

