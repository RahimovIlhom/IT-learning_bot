from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu')],
    ],
    resize_keyboard=True
)
