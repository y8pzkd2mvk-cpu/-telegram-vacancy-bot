import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile

# ================= НАСТРОЙКИ =================

import os

# Укажи чаты, где размещение объявлений разрешено.
# Для публичных чатов/каналов можно использовать @username.
# Для закрытых групп обычно нужен числовой chat_id, например -1001234567890.
CHAT_IDS = [
    "@MyWorkON_EKB",
    "@tumenwork1",
    "@EKB_Rabota_1",
]

# Публиковать раз в 24 часа.
# Публиковать каждые 10 минут.
PUBLISH_INTERVAL_MINUTES = 10

IMAGE_PATH = "vacancy.jpg"

TEXT = """🛒 ЯНДЕКС ЛАВКА — ИЩЕМ КЛАДОВЩИКА

💰 Новички тоже могут заработать от 100 000 ₽ в месяц!

👤 КТО МОЖЕТ УСТРОИТЬСЯ?

🔹 Возраст: 18–55 лет
🔹 Самозанятые и ИП
🔹 Граждане РФ и стран ЕАЭС

✨ ЧТО МЫ ПРЕДЛАГАЕМ?

📄 Официальное оформление по ТК РФ
💳 Выплаты 2 раза в месяц
📅 График 5/2, выходные плавающие
⏰ 8-часовой рабочий день
🌅 Утренняя смена: 7:00–16:00
🌙 Вечерняя смена: 15:00–00:00
🔄 Смены чередуются
🏥 ДМС: частные клиники и стоматология
📋 Бесплатное оформление медкнижки
🍲 Комплексный обед — 95 ₽

📦 ЧЕМ ПРЕДСТОИТ ЗАНИМАТЬСЯ?

▫️ Разгружать товар
▫️ Размещать товар на стеллажах и в морозильной камере
▫️ Собирать и упаковывать заказы
▫️ Передавать готовые заказы курьерам
▫️ Поддерживать чистоту и порядок на складе

🚀 ГОТОВ НАЧАТЬ?

👉 ТРУДОУСТРОИТЬСЯ:
https://trk.ppdu.ru/click/cHyOQj2u?erid=CQH36pWzJqVGXC5oUHvq1FTH2g3oi1KL72bsqkyo9iVXM7
"""

# =============================================

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()


async def publish(bot: Bot):
    image = Path(IMAGE_PATH)

    for chat_id in CHAT_IDS:
        try:
            if image.exists():
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=FSInputFile(image),
                    caption=TEXT,
                )
            else:
                await bot.send_message(chat_id=chat_id, text=TEXT)

            logging.info("Опубликовано: %s", chat_id)

        except Exception:
            logging.exception("Ошибка публикации в %s", chat_id)

        # Небольшая пауза между чатами.
        await asyncio.sleep(5)


async def main():
    BOT_TOKEN = os.environ["BOT_TOKEN"]
        raise RuntimeError("Сначала вставь токен бота в BOT_TOKEN.")

    bot = Bot(BOT_TOKEN)

    try:
        while True:
            await publish(bot)
            logging.info(
                "Следующая публикация через %s минут.",
                PUBLISH_INTERVAL_MINUTES,
            )
            await asyncio.sleep(PUBLISH_INTERVAL_MINUTES * 60)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
