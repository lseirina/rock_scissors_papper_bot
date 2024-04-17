from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

group_name = 'aiogram_stepik_course'
url_button_1 = InlineKeyboardButton(
    text='Telegrambot on Aiogram',
    url=f'tg://resolve?domain={group_name}'
)
channel_name = 'toBeAnMLspecialist'
url_button_2 = InlineKeyboardButton(
    text='Chennel for MLspecialist',
    url=f'https://t.me/{channel_name}'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='These are inlinebuttons with "url"',
        reply_markup=keyboard
    )


if __name__ == "__main__":
    dp.run_polling(bot)