from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None):
    env: Env = Env()
    env.read_env()

    config = Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )

    return config