from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = getenv("bot_token")
openai_api_token = getenv("openai_key")

# Теперь файл базы данных будет именно "bazadanyx"
DB_FILE = "bazadanyx"

class DataBaseSettings():
    # Файл БД с использованием SQLite + aiosqlite
    url: str = f"sqlite+aiosqlite:///{DB_FILE}"
    echo: bool = False

class OpenAISettings():
    token: str = openai_api_token

class BotSettings():
    token: str = TOKEN

class Settings():
    bot: BotSettings = BotSettings()
    openai: OpenAISettings = OpenAISettings()
    db: DataBaseSettings = DataBaseSettings()

settings = Settings()
