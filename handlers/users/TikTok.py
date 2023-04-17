from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text

@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def tiktok(message: types.Message):
    await message.answer("TikTok")  