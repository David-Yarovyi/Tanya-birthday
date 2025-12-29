from aiogram import Router,  F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

def congr_menu():
    tb = InlineKeyboardBuilder()
    tb.button(text="⬅ Назад", callback_data="back_to_menu")
    tb.adjust(1)
    return tb.as_markup()