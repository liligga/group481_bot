from aiogram import Router, F, types
from aiogram.filters import Command

from bot_config import database
from pprint import pprint


shop_router = Router()


@shop_router.message(Command("books"))
async def show_all_books(message: types.Message):
    book_list = database.get_all_books()
    pprint(book_list)
    # for book in book_list:
    #     txt = f"Название: {book[1]}\nЦена: {book[2]}"
    #     await message.answer(txt)
    for book in book_list:
        cover = book['cover']
        print("Book cover", cover)
        txt = f"Название: {book['name']}\nЦена: {book['price']}\nЖанр: {book['genre']}"
        await message.answer_photo(
            photo=cover,
            caption=txt
        )

