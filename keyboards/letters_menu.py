from aiogram import Bot, Router, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

def letters_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="👩 Света", callback_data="letter_mom")
    kb.button(text="👨 Леша", callback_data="letter_dad")
    kb.button(text="👦🏽 Давид", callback_data="letter_nephew")
    kb.button(text="👵 Мама", callback_data="letter_grandma")
    kb.button(text="⬅ Назад", callback_data="back_to_menu")
    kb.adjust(1)
    return kb.as_markup()

def letters_under_menu():
    bt = InlineKeyboardBuilder()
    bt.button(text="⬅ Назад", callback_data="back_to_letters")
    bt.adjust(1)
    return bt.as_markup()