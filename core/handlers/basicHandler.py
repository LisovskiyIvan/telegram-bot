from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keys.reply import random_anime_kb
import requests
import json 



basicRouter = Router()


@basicRouter.message(F.text == 'Рандомное аниме')
async def get_anime(message: Message):
    anime = requests.get('https://api.jikan.moe/v4/random/anime').json()

    title_rom = anime.get("data").get("title")
    title_en = anime.get("data").get("title_english")
    if title_en == None:
        title = title_rom
    else:
        title = title_en

    title_jp = anime.get("data").get("title_japanese")
    description = anime.get("data").get("synopsis")
    if description == None:
        description = 'Не указано'


    genres = anime.get("data").get("genres")


    if (genres != []):
        arr = []
        str = ''
        for genre in genres:
            arr.append(genre.get('name'))
            
        for item in arr:
            str = str + item + '\n'
    else:
        str = 'Не указаны\n'

    img = anime.get("data").get("images").get('jpg').get('large_image_url')
    age = anime.get("data").get("rating")
    age_str = f'Возрастной рейтинг: {age}'
    score = anime.get("data").get("score")
    if score == None:
        score_str = ''
    else:
        score_str = f'Рейтинг: {score}'
    episodes = anime.get("data").get("episodes")
    episodes_str = f'Количество эпизодов: {episodes}'
    res = f'{score_str}\n\n{title}\n{title_jp}\n\nОписание: {description}\n\nЖанры:\n{str}\n{episodes_str}\n\n{age_str}'

    await message.answer_photo(img)
    await message.answer(res, reply_markup=random_anime_kb)
@basicRouter.message(F.text == 'В начало')

    
@basicRouter.message(F.text == 'Список предметов')
async def get_archive(message: Message):
    await message.answer()

@basicRouter.message(F.text == 'Правила')
async def get_archive(message: Message):
    await message.answer()

@basicRouter.message(F.text == 'Стать исполнителем')
async def get_archive(message: Message):
    await message.answer()
    