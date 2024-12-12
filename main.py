import asyncio
import logging

from bot_config import dp, bot, database
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.other_messages import echo_router
from handlers.dialog import opros_router


async def on_startup(bot):
    database.crate_tables()


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(opros_router)

    # в самом конце
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
