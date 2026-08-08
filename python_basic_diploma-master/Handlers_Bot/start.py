from aiogram import types, Dispatcher
from aiogram.filters import Command
from Handlers_Bot.find import find_command
from Keyboard.main_menu import main_menu
from Handlers_Bot.history import history_command, clear_history_command
from Handlers_Bot.help import help_command

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def start_command(message: types.Message):
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!\n\n"
            "🍽 Я твой ресторанный помощник — всегда рядом, чтобы подсказать лучшие места для вкусного отдыха!\n\n"
            "✨ Что я умею:\n"
            "• Найти ресторан по типу кухни\n"
            "• Показать историю твоих запросов\n"
            "• Подсказать команды и возможности\n\n"
            "👇 Выбери действие ниже и начнём путешествие по вкусам!",
            reply_markup=main_menu
        )

    @dp.message(lambda m: m.text == "🍣 Суши")
    async def process_sushi(message: types.Message):
        await find_command(message, "суши")

    @dp.message(lambda m: m.text == "🍕 Пицца")
    async def process_pizza(message: types.Message):
        await find_command(message, "пицца")

    @dp.message(lambda m: m.text == "📜 История")
    async def process_history(message: types.Message):
        await history_command(message)

    @dp.message(lambda m: m.text == "❓ Помощь")
    async def process_help(message: types.Message):
        await help_command(message)

    @dp.message(lambda m: m.text == "🗑️ Очистить историю")
    async def process_clear_history(message: types.Message):
        await clear_history_command(message)









