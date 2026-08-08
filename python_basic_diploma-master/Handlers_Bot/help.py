from aiogram import types, Dispatcher
from aiogram.filters import Command

async def help_command(message: types.Message):
    await message.answer(
        "❓ Вот список команд:\n"
        "/start — приветствие\n"
        "/help — список команд\n"
        "/find <кухня> — поиск ресторана\n"
        "/history — история запросов"
    )

def register_handlers(dp: Dispatcher):
    dp.message.register(help_command, Command("help"))


