from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Рандомное аниме'
        ),
        KeyboardButton(
            text='Рандомная манга'
        )
    ],
    [
        KeyboardButton(
            text='Правила'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку', selective=True)


archive_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Архив 1', url='https://music.yandex.ru/home')],
    [InlineKeyboardButton(text='Архив 2', url='https://music.yandex.ru/home')]
])

subjects = {
    '1': 'Математика',
    '2': 'Информатика',
    '3': 'Ландшафтная архитектура'
}

rules = 'Тут будут правила:\n1. Первое правило клуба\n2. Второе правило клуба'

random_anime_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рандомное аниме')],
    [KeyboardButton(text='Назад')]
],  resize_keyboard=True, one_time_keyboard=True)

become_partner = 'А тут будут условия или контакты чтобы стать партнером'