from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

big_bitton_1 = InlineKeyboardButton(
    text='Big button 1',
    callback_data='button_1_pressed'
)
big_button_2 = InlineKeyboardButton(
    text='Big button 2',
    callback_data='button_2_pressed'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_bitton_1], [big_button_2]]
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='These are inline buttons',
        reply_markup=keyboard
    )


@dp.callback_query(F.data == 'button_1_pressed')
async def process_1_btn_press(callback: CallbackQuery):
    if callback.message.text != 'The first button was pressed':
        await callback.message.edit_text(
            text='The first button was pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(
        text='The first button is pressed!'
    )


@dp.callback_query(F.data == 'button_2_pressed')
async def process_2_btn_press(callback: CallbackQuery):
    if callback.message.text != 'The second button was pressed':
        await callback.message.edit_text(
            text='The second button was pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(
        text='The second button was pressed',
        show_alert=True
    )


if __name__ == "__main__":
    dp.run_polling(bot)