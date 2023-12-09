from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import ContentType

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


@dp.message_handler(content_types=[ContentType.VIDEO])
async def send_video(msg: types.Message):
    await msg.answer(msg.video.file_id)
