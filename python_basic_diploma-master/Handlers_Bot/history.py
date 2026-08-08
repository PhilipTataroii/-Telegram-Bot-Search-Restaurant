from aiogram import types, Dispatcher
from aiogram.filters import Command
from Handlers_Bot.models import History

async def history_command(message: types.Message):
    records = History.select().where(History.user_id == message.from_user.id)
    if records:
        text = "📜 История запросов:\n" + "\n".join([f"- {r.query}" for r in records])
        await message.answer(text)
    else:
        await message.answer("История пуста.")

async def clear_history_command(message: types.Message):
    deleted = History.delete().where(History.user_id == message.from_user.id).execute()
    if deleted:
        await message.answer("🗑 История успешно очищена!")
    else:
        await message.answer("История уже пустая.")

def register_handlers(dp: Dispatcher):
    dp.message.register(history_command, Command("history"))
    dp.message.register(clear_history_command, Command("clear_history"))




