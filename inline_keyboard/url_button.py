from aiogram import Bot, Dispatcher
from aiogram.filters import (CommandStart)
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

url_button_1 = InlineKeyboardButton(
    text='Course "Telegrambot in python"',
    url='https://stepik.org/120924',
)
url_button_2 = InlineKeyboardButton(
    text='Telegrambot API documentation',
    url='https://core.telegram.org/bots/api'
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
