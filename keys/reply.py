from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Случайное аниме'
        ),
        KeyboardButton(
            text='Случайная манга'
        )
    ],
    [
        KeyboardButton(
            text='Кто я?'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку', selective=True)


archive_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Архив 1', url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text='Архив 2', url='https://music.yandex.ru/home')]
])


random_anime_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Случайное аниме')],
    [KeyboardButton(text='Назад')]
],  resize_keyboard=True, one_time_keyboard=True)

random_manga_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Случайная манга')],
    [KeyboardButton(text='Назад')]
],  resize_keyboard=True, one_time_keyboard=True)

go_back_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Назад')]
],  resize_keyboard=True, one_time_keyboard=True)
