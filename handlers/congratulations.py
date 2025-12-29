from aiogram import  Router, F, types
from keyboards.congratulations import congr_menu
from keyboards.main_menu import main_menu_kb

router = Router()

@router.callback_query(F.data == 'congratulations')
async def show_letters(callback : types.CallbackQuery):
    await callback.message.edit_text(
        "🎉 Дорогая тётя! 🎉\nС днём рождения! 💖\nТы невероятно сильная, умная и вдохновляющая. \nПусть работа приносит не только успех и развитие, но и удовольствие.\nПусть солнечная Испания станет для тебя местом спокойствия, радости и новых возможностей 🌞🇪🇸\nЖелаем счастья в личной жизни, гармонии, любви и тёплых моментов рядом с близким человеком 💫\nПусть каждый новый день дарит уверенность, улыбки и веру в лучшее будущее.",
        reply_markup= congr_menu()
    )
    await callback.answer()

@router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню",
        reply_markup=main_menu_kb()
    )
    await callback.answer()
