from aiogram import Bot, Router, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.main_menu import main_menu_kb


router = Router()

@router.message(Command('start'))
async def main_menu(message: types.Message):
    await message.answer(
        "💖 Дорогая Таня! \nСегодня особенный день — этот бот создан специально для тебя 🎉🎉🎉 \nВыбирай, что хочешь открыть ✨",
        reply_markup=main_menu_kb()
    )
