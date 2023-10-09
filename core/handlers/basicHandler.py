from aiogram import Router, F
from aiogram.types import Message
from keys.reply import random_anime_kb, random_manga_kb, reply_keyboard, go_back_kb
import requests
from googletrans import Translator



basicRouter = Router()

def trans(text, src='en', dest='ru'):
    translator = Translator()
    translation = translator.translate(text=text, src=src, dest=dest)
    return translation.text



@basicRouter.message(F.text == 'Случайное аниме')
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
        description = ' Не указано'
    description = trans(text=description)

    genres = anime.get("data").get("genres")


    if (genres != []):
        arr = []
        genres_str = ''
        for genre in genres:
            arr.append(genre.get('name'))
            
        for item in arr:
            genres_str = genres_str + item + '\n'
        genres_str = trans(text=genres_str)
    else:
        genres_str = 'Не указаны\n'

    img = anime.get("data").get("images").get('jpg').get('large_image_url')
    age = anime.get("data").get("rating")
    age_str = f'Возрастной рейтинг: {age}'
    score = anime.get("data").get("score")
    if score == None:
        score_str = ''
    else:
        score_str = f'Рейтинг: {score}'
    episodes = anime.get("data").get("episodes")
    if episodes == None:
        episodes_str = 'Не указано'
    episodes_str = f'Количество эпизодов: {episodes}'
    res = f'{score_str}\n\n{title}\n{title_jp}\n\nОписание: {description}\n\nЖанры: {genres_str}\n\n{episodes_str}\n\n{age_str}'

    await message.answer_photo(img)
    await message.answer(res, reply_markup=random_anime_kb)

    
@basicRouter.message(F.text == 'Случайная манга')
async def get_manga(message: Message):
    manga = requests.get("https://api.jikan.moe/v4/random/manga").json()

    title_rom = manga.get("data").get("title")
    title_en = manga.get("data").get("title_english")
    if title_en == None:
        title = title_rom
    else:
        title = title_en

    title_jp = manga.get("data").get("title_japanese")
    description = manga.get("data").get("synopsis")
    if description == None:
        description = "Не указано"
    description = trans(text=description)

    themes = manga.get("data").get("themes")
    if themes != []:
        arr = []
        themes_str = ""
        for theme in themes:
            arr.append(theme.get("name"))

        for x in arr:
            themes_str = themes_str + x + "\n"
        themes_str = trans(text=themes_str)
    else:
        themes_str = ""

    genres = manga.get("data").get("genres")


    if genres != []:
        arr = []
        genres_str = ""
        for genre in genres:
            arr.append(genre.get("name"))

        for x in arr:
            genres_str = genres_str + x + "\n"
        genres_str = trans(text=genres_str)
    else:
        genres_str = "Не указаны\n"

    img = manga.get("data").get("images").get("jpg").get("large_image_url")


    authors = manga.get("data").get("authors")
    if authors != []:
        arr = []
        auth = ""
        for genre in authors:
            arr.append(genre.get("name"))

        for x in arr:
            auth = auth + x + " "
        authors_str = f'Авторы: {auth}'
    else:
        authors_str = "Не указан\n"

    response = f"{title}\n{title_jp}\n\nОписание: {description}\n\nЖанры: {genres_str}{themes_str}\n\n{authors_str}"
    await message.answer_photo(img)
    await message.answer(response, reply_markup=random_manga_kb)
    
@basicRouter.message(F.text == 'Кто я?')
async def get_rules(message: Message):
    await message.answer("Привет! Меня зовут Канеки Кен бот, я ЕБАНУТЫЙ НА ГОЛОВУ СКОРОСТЬ УДАРИЛА В ГОЛОВУ и моя суть - это подсказать тебе случайное аниме или мангу. Надеюсь ты найдешь что-то интересное!", reply_markup=go_back_kb)

@basicRouter.message(F.text == 'Назад')
async def get_start(message: Message):
    await message.answer('Старт', reply_markup=reply_keyboard)
