from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

big_button_1 = InlineKeyboardButton(
    text='Big button 1',
    callback_data='big_button_1_pressed',
)
big_button_2 = InlineKeyboardButton(
    text='Big button 2',
    callback_data='big_button_2_pressed'
)


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1], [big_button_2]]
)


@dp.message(CommandStart())
async def process_button_press(message: Message):
    await message.answer(
        text='These are inline buttons. Press any',
        reply_markup=keyboard
    )


@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'big_button_1_was_pressed':
        await callback.message.edit_text(
            text='big_button_1_was_pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'big_button_2_was_pressed':
        await callback.message.edit_text(
            text='big_button_2_was_pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


if __name__ == "__main__":
    dp.run_polling(bot)
