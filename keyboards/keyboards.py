from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

yes_button = KeyboardButton(text=LEXICON_RU['yes_button'])
no_button = KeyboardButton(text=LEXICON_RU['no_button'])

y_n_kb = ReplyKeyboardBuilder()
y_n_kb.row(yes_button, no_button, width=2)

yes_no_keyboard_1 = y_n_kb.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


btn_rock = KeyboardButton(text=LEXICON_RU['rock'])
btn_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
btn_papper = KeyboardButton(text=LEXICON_RU['papper'])

game_kebord = ReplyKeyboardMarkup(
    keyboard=[[btn_rock],
              [btn_scissors],
              [btn_papper]],
    resize_keyboard=True
)
