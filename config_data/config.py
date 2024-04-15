from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    database: DatabaseConfig


def load_config(path: str | None = None):
    env: Env = Env()
    env.read_env()

    config = Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        database=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
        )
    )
