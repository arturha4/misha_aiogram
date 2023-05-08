from aiogram import Bot, Dispatcher, executor, types
from incommand import ikb, kb, InlineKeyboardMarkup, InlineKeyboardButton
from beton import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP ="""
<em>/help</em> - <b>список команд</b>
<em>/photo</em> - <b>отправляет фотографию</b>
<em>/links</em> - <b>нужные ссылк в интернет</b>
<em>/vote</em> - <b>даёт фото на оценку</b>"""

async def on_startup(_):
    print('Программа запущена, Сэр!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Здравствуйте Сэр!',
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['links'])
async def command_links(message: types.Message):
    await message.answer(text='Выбирете опцию ...',
                         reply_markup=ikb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer(text=HELP,
                         reply_markup=kb,
                         parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['photo'])
async def send_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://zastavok.net/leto/63383-holmy_zelen_ris.html',
                         reply_markup=kb)
    await message.delete()

@dp.callback_query_handler()
async def send_command_agter_callback(callback: types.CallbackQuery):
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo='https://zastavok.net/leto/63383-holmy_zelen_ris.html',
                         reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb2 =InlineKeyboardMarkup(row_width=2)
    ib3 = InlineKeyboardButton(text='❤️',
                               callback_data='like')
    ib4 = InlineKeyboardButton(text='👎',
                               callback_data='dislike')
    ikb2.add(ib3, ib4)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://i.7fon.org/1000/f64433345.jpg',
                         caption='Нравиться картинка?',
                         reply_markup=ikb2)

@dp.callback_query_handler()
async def send_query(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Ух ты, тебе нравился мой выбор')
    await send_command_agter_callback(callback)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
