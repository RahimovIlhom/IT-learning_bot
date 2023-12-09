from aiogram import types

from keyboards.inline import create_category_buttons, create_subcategory_buttons, create_lessons_buttons, \
    create_video_buttons
from keyboards.inline.callBack_query import callback_data
from loader import dp, db


@dp.message_handler(text='Menu')
async def show_categories(message, **kwargs):
    if isinstance(message, types.Message):
        await message.answer("Kategoriyani tanglang", reply_markup=create_category_buttons())
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text("Kategoriyani tanglang", reply_markup=create_category_buttons())


async def show_subcategories(call: types.CallbackQuery, category_id, **kwargs):
    await call.message.edit_text("Kursni tanlang:", reply_markup=create_subcategory_buttons(category_id))


async def show_lessons(call: types.CallbackQuery, category_id, subcategory_id, **kwargs):
    await call.message.delete()
    await call.message.answer("Darsni tanlang: ", reply_markup=create_lessons_buttons(category_id, subcategory_id))


async def show_lesson(call: types.CallbackQuery, category_id, lesson_id, **kwargs):
    id, video_id, video_url, title, body, subcategory_id = db.select_lesson(lesson_id)
    await call.message.delete()
    await call.message.answer_video(video=video_id, caption=f"{id}-video dars.\n\n{title}\n\n{body}",
                                    reply_markup=create_video_buttons(category_id, subcategory_id, lesson_id))


@dp.callback_query_handler(callback_data.filter())
async def send_message(call: types.CallbackQuery, callback_data: dict):
    level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    lesson = callback_data.get('lesson')
    if level == '0':
        func_name = show_categories
    elif level == '1':
        func_name = show_subcategories
    elif level == '2':
        func_name = show_lessons
    elif level == '3':
        func_name = show_lesson
    else:
        await call.message.delete()
        return

    await func_name(call, category_id=category, subcategory_id=subcategory, lesson_id=lesson)
