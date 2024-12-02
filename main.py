import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")

@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)




async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

