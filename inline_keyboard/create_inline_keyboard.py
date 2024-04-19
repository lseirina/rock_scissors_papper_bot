from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',
}
BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'
}


def create_inline_kb(width, *args, **kwargs):
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
               text=LEXICON[button] if button in LEXICON else button,
               callback_data=button
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(2, 'btn_1', 'btn_2', 'btn_3')
    await message.answer(
        text='This keyboard is formated by'
             '<code>create_inline_kb</code>',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
