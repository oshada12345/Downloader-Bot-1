from aiogram import types
from pytube import YouTube
from loader import dp
import os

@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    link = message.text
    yt = YouTube(link)
    if message.text.startswith == "https://youtu.be/" or "https://www.youtube.com/":
            stream = yt.streams.filter(progressive=True, file_extension='mp4')
            stream.get_highest_resolution().download(f'f{message.chat.id}', f'{message.chat.id}_{yt.title}')
            with open (f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
                await message.answer_video(video=video)
                os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
    else:
        await message.answer("Bat Command🤨")

# async def Download_you_tube(link, message):
#     yt = YouTube(link)
#     stream = yt.streams.filter(progressive=True, file_extension='mp4')
#     stream.get_highest_resolution().download(f'f{message.chat.id}', f'{message.chat.id}_{yt.title}')
#     with open (f'{message.chat.id}_{yt.title}', 'rb') as video:
#         await message.answer_video(video=video)