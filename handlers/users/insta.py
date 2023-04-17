from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def insta(message: types.Message):
    await message.answer("Instagram")