import os
from config import settings
from config import DB_FILE  # если нужно, иначе можно извлечь из настроек

from config import settings  # для получения настроек через settings
from sqlalchemy import String, BIGINT
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

class PomodoroUser(Base):
    user_id: Mapped[int] = mapped_column(BIGINT)

class User(Base):
    user_id: Mapped[int] = mapped_column(BIGINT)
    datetime: Mapped[str] = mapped_column(String)

class Train(Base):
    user_id: Mapped[int] = mapped_column(BIGINT)
    answers: Mapped[str] = mapped_column(String)

class InfoTraining(Base):
    user_id: Mapped[int] = mapped_column(BIGINT)
    answers: Mapped[str] = mapped_column(String)

class ReflectAnswers(Base):
    user_id: Mapped[int] = mapped_column(BIGINT)
    answers: Mapped[str] = mapped_column(String)

# Асинхронная инициализация базы: создание таблиц, если их нет
async def init_db(engine):
    # Извлекаем путь к файлу из URL
    db_file = settings.db.url.split("///")[-1]
    if not os.path.exists(db_file):
        # Создаем пустой файл для БД, если он не существует
        open(db_file, "a").close()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
if __name__ == '__main__':
    import asyncio
    asyncio.run(init_db())
