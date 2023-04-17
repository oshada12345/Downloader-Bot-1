from pytube import  YouTube
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
import aiofiles
import os
import time

@dp.message_handler(Text(startswith='https://www.youtube.com/'))
async def you_tube(message: types.Message):
    # await message.answer("Downloading...")
    # message_animation = await message.answer(text="Downloading...")
    # for i in range(1,11):
    #     text0 = i*10
    #     await message_animation.edit_text(f"{text0}%")
    #     await message_animation.delete()
    
    link = message.text
    yt = YouTube(link)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download('media/', f'{message.chat.id}.mp4')
    async with aiofiles.open(f"D:/Python1/Fullbot/pytube/Downloader-Bot/media/{message.chat.id}.mp4", "rb") as file:
        if yt.length > 60:
            time55 = yt.length // 60
            time_residual = yt.length % 60
            await message.answer_video(video=file, caption=f"Video Title: {yt.title}\n\nVideo Author: {yt.author}\n\nNumber of views: {yt.views} time\n\nVideo Duration: {time55} minute {time_residual} second")
            time.sleep(10)
            # file.close()
            os.remove(f"D:/Python1/Fullbot/pytube/Downloader-Bot/media/{message.chat.id}.mp4")
        else:
            await message.answer_video(video=file, caption=f"Video Title: {yt.title}\n\nVideo Author: {yt.author}\n\nNumber of views: {yt.views} time\n\nVideo Duration: {yt.length} second")
            time.sleep(10)
            # file.close()
            os.remove(f"D:/Python1/Fullbot/pytube/Downloader-Bot/media/{message.chat.id}.mp4")