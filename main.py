import asyncio
import logging

from bot_config import dp, bot, database
from handlers import private_router
from handlers.group_management import group_router

async def on_startup(bot):
    database.crate_tables()


async def main():
    # регистрация роутеров
    dp.include_router(private_router)
    dp.include_router(group_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
