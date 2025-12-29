from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.letters_menu import letters_menu, letters_under_menu
from keyboards.main_menu import main_menu_kb
from data.letters import LETTERS

router = Router()

@router.callback_query(F.data == 'letters')
async def show_letters(callback : types.CallbackQuery):
    await callback.message.edit_text(
        "Выбери, от кого письмо:",
        reply_markup= letters_menu()
    )
    await callback.answer()

@router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню",
        reply_markup=main_menu_kb()
    )
    await callback.answer()

@router.callback_query(F.data == 'back_to_letters')
async def back_to_letters(callback : types.CallbackQuery,  state:FSMContext):
    await callback.message.edit_text(
        "Выбери, от кого письмо:",
        reply_markup=letters_menu()
    )

    data = await state.get_data()
    voice_msg_id = data.get("voice_msg_id")

    if voice_msg_id:
        await callback.bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=voice_msg_id
        )
        await state.update_data(voice_msg_id=None)



    await callback.answer()


@router.callback_query(F.data.startswith('letter_'))
async def show_letter(callback : types.CallbackQuery,  state:FSMContext):
    letter_id = callback.data.replace('letter_' , '')
    letter = LETTERS.get(letter_id)

    if not letter:
        letter_text = 'Письмо не найдено'
    else : 
        letter_text = letter['text']

    if letter and letter.get("voice"):
        voice = FSInputFile(letter["voice"])
        voice_msg = await callback.message.answer_voice(voice)

        await state.update_data(
            voice_msg_id=voice_msg.message_id
        )
    

    await callback.message.edit_text(letter_text, reply_markup=letters_under_menu())
    await callback.answer()
    
    




