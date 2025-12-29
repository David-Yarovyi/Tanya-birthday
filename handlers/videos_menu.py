from aiogram import F, Router, types
from keyboards.main_menu import main_menu_kb
from data.videos_date.videos import VIDEOS
from keyboards.photo_and_videos import show_photos_kb, back_to_photo_menu
from aiogram.types import FSInputFile

router = Router()

@router.callback_query(F.data == 'video')
async def show_video_menu(callback : types.CallbackQuery):
    await callback.message.delete()

    await callback.message.bot.send_video(
        chat_id=callback.message.chat.id,
        video=FSInputFile(VIDEOS[0]),
        caption='Видео-поздравление 🎬' 
    )

    await callback.message.bot.send_message(
        chat_id=callback.message.chat.id,
        text='⬅ Вернуться назад',
        reply_markup=back_to_photo_menu()
    )

    await callback.answer()
