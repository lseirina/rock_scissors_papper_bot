from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def set_new_manu(bot: Bot):
    new_manu = [
        BotCommand(
            command='/help',
            description='Help'
        ),
        BotCommand(
            command='/contects',
            description='other contects'
        ),
        BotCommand(
            command='/payment',
            description='payment'
        )
    ]
    await bot.set_my_commands(new_manu)

dp.startup.register(set_new_manu)
dp.run_polling(bot)
