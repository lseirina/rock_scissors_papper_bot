from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

@router.message()
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
