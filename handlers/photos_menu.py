from aiogram import F, Router, types
from keyboards.main_menu import main_menu_kb
from data.photos_date.photos import PHOTOS
from keyboards.photo_and_videos import show_photos_kb, back_to_photo_menu
from aiogram.types import FSInputFile, InputMediaPhoto

router = Router()

@router.callback_query(F.data == 'photos_and_videos')
async def show_photos_menu(callback : types.CallbackQuery):
    await callback.message.edit_text(text='📸 Здесь собраны тёплые моменты, фото и видео', 
                                     reply_markup=show_photos_kb()
                                     )

    await callback.answer()


@router.callback_query(F.data == 'back_to_photo_menu')
async def back_to_ph_menu(callback : types.CallbackQuery):
    await callback.message.edit_text(
        text="📸 Здесь собраны тёплые моменты, фото и видео",
        reply_markup=show_photos_kb()
    )
    await callback.answer()


@router.callback_query(F.data == 'photos')
async def show_album(callback: types.CallbackQuery):
    await callback.message.delete()
    media = []

    for i, photo_path in enumerate(PHOTOS):
        if i == 0:
            media.append(
                InputMediaPhoto(
                    media = FSInputFile(photo_path),
                    caption="📸 Самые тёплые моменты 💛"
                )
            )
        else :
            media.append(
                InputMediaPhoto(
                    media=FSInputFile(photo_path)
                )
            )
    await callback.message.bot.send_media_group(
        chat_id=callback.message.chat.id,
        media=media
    )

    await callback.message.bot.send_message(
            chat_id=callback.message.chat.id,
            text="⬅ Вернуться назад",
            reply_markup=back_to_photo_menu()
        )
    await callback.answer()



