from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍣 Суши")],
        [KeyboardButton(text="🍕 Пицца")],
        [KeyboardButton(text="📜 История")],
        [KeyboardButton(text="❓ Помощь")],
        [KeyboardButton(text="🗑️ Очистить историю")]
    ],
    resize_keyboard=True
)


