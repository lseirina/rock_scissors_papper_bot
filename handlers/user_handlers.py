from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import (
    game_keybord,
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
        reply_markup=game_keybord
    )
