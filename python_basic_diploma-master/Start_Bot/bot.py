import asyncio
import logging
from aiogram import Bot, Dispatcher
from Token_and_Database.config import BOT_TOKEN
from Handlers_Bot import start, help, find, history

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # подключаем обработчики
    start.register_handlers(dp)
    help.register_handlers(dp)
    find.register_handlers(dp)
    history.register_handlers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())





