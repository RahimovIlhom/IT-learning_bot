from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callBack_query import create_callback_data
from loader import db


def create_category_buttons():
    CURRENT_LEVEL = 0
    categories = db.select_categories()
    markup = InlineKeyboardMarkup(row_width=3)
    for id, category in categories:
        markup.insert(
            InlineKeyboardButton(
                text=category, callback_data=create_callback_data(level=CURRENT_LEVEL+1, category=id)
            )
        )
    markup.row(
        InlineKeyboardButton(
            text="❌",
            callback_data=create_callback_data(level=CURRENT_LEVEL-1)
        )
    )
    return markup


def create_subcategory_buttons(category):
    CURRENT_LEVEL = 1
    subcategories = db.select_sub_categories_in(category)
    markup = InlineKeyboardMarkup(row_width=2)
    for id, subcategory, category_id in subcategories:
        markup.insert(
            InlineKeyboardButton(
                text=subcategory,
                callback_data=create_callback_data(CURRENT_LEVEL+1, category=category, subcategory=id)
            )
        )
    markup.row(
        InlineKeyboardButton(
            text="🔙 Back",
            callback_data=create_callback_data(level=CURRENT_LEVEL-1)
        )
    )
    return markup


def create_lessons_buttons(category_id, subcategory):
    CURRENT_LEVEL = 2
    lessons = db.select_sub_category_lessons(subcategory)
    markup = InlineKeyboardMarkup(row_width=3)
    for id, video_id, video_url, title, body, subcategory_id in lessons:
        markup.insert(
            InlineKeyboardButton(
                text=f"{id}-dars",
                callback_data=create_callback_data(CURRENT_LEVEL+1, category=category_id, lesson=id)
            )
        )
    markup.row(
        InlineKeyboardButton(
            text='🔙 Back',
            callback_data=create_callback_data(level=CURRENT_LEVEL-1, category=category_id)
        )
    )
    return markup


def create_video_buttons(category_id, subcategory_id, lesson_id):
    CURRENT_LEVEL = 3
    lesson = db.select_lesson(lesson_id)
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(InlineKeyboardButton(text="Site orqali", url=lesson[2]))
    markup.row(
        InlineKeyboardButton(
            text='🔙 Back',
            callback_data=create_callback_data(level=CURRENT_LEVEL-1, category=category_id, subcategory=subcategory_id)
        )
    )
    return markup
