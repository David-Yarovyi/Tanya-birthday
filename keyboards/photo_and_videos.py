from aiogram.utils.keyboard import InlineKeyboardBuilder

def show_photos_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='📷 Фото', callback_data='photos')
    kb.button(text='🎥 Видео', callback_data='video')
    kb.button(text='⬅ Назад', callback_data='back_to_menu')

    kb.adjust(1)
    return kb.as_markup()

def back_to_photo_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text='⬅ Назад', callback_data='back_to_photo_menu')

    kb.adjust(1)
    return kb.as_markup()

