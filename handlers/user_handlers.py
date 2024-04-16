from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import (
    game_keyboard,
    yes_no_keyboard,
)
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=yes_no_keyboard
    )


@router.mesage(Command(commands='help'))
async def process_help_command(message: Message):
    message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=yes_no_keyboard
    )


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=game_keyboard
    )


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['no'],
        reply_markup=yes_no_keyboard
    )


@router.message(F.text.in_(
    LEXICON_RU['rock'],
    LEXICON_RU['scissors'],
    LEXICON_RU['papper'])
)
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}-'
                              f'{LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_keyboard)
