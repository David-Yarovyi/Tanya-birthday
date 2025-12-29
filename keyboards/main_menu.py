from aiogram import Bot, Router, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu_kb():
    bt = InlineKeyboardBuilder()
    bt.button(text="Общее поздравление", callback_data = "congratulations")
    bt.button(text="Фото и видео", callback_data='photos_and_videos')
    bt.button(text="💌 Письма от семьи", callback_data="letters")
    bt.adjust(1)
    return bt.as_markup()
