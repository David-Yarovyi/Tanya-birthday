from aiogram import F, Router, types
from keyboards.main_menu import main_menu_kb
from data.photos_date.photos import PHOTOS
from keyboards.photo_and_videos import show_photos_kb, back_to_photo_menu
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(F.data == 'video')
async def show_video_menu(callback : types.CallbackQuery):
    await callback.message.edit_text(
        text='Видео-поздравление 🎬',
        reply_markup=back_to_photo_menu()
    )