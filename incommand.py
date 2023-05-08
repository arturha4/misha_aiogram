from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Yandex',
                           url='https://yandex.ru/search/?text=%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81&clid=2411726&lr=10991')
ib2 = InlineKeyboardButton(text='YouTube',
                           url='https://www.youtube.com/@KINOKOS')

ikb.add(ib1, ib2)
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
v1 = KeyboardButton(text='/links')
v2 = KeyboardButton(text='/help')
v3 = KeyboardButton(text='/photo')
v4 = KeyboardButton(text='/vote')
kb.add(v1).insert(v2).add(v3).insert(v4)