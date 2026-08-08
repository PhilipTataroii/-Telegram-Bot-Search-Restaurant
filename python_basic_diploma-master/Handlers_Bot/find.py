from aiogram import types, Dispatcher
from aiogram.filters import Command
from Handlers_Bot.models import Restaurant, History

async def find_command(message: types.Message, query: str = None):
    if query is None:
        query = message.text.replace("/find", "").strip().lower()
    else:
        query = query.strip().lower()

    if query:
        History.create(user_id=message.from_user.id, query=query)
        results = Restaurant.select().where(Restaurant.cuisine.contains(query))
        if results:
            for r in results:
                text = (
                    f"🍴 {r.name}\n"
                    f"📍 {r.address}\n"
                    f"📞 {r.phone}\n"
                    f"✉️ {r.email}\n"
                    f"🌐 [Сайт]({r.website})"
                )
                if r.image_url:
                    await message.answer_photo(
                        photo=r.image_url,
                        caption=text,
                        parse_mode="Markdown"
                    )
                else:
                    await message.answer(text, parse_mode="Markdown")
        else:
            await message.answer("😔 Не нашёл ресторанов по такому запросу.")
    else:
        await message.answer("Напиши, что искать. Например: /find суши")

def register_handlers(dp: Dispatcher):
    dp.message.register(find_command, Command("find"))





