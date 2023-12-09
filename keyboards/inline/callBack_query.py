from aiogram.utils.callback_data import CallbackData

callback_data = CallbackData('menu', 'level', 'category', 'subcategory', 'lesson')


def create_callback_data(level, category='0', subcategory='0', lesson='0'):
    return callback_data.new(level=level, category=category, subcategory=subcategory, lesson=lesson)
