from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext

from bot_config import database
from pprint import pprint


book_management_router = Router()
book_management_router.message.filter(F.from_user.id == 243154734)
book_management_router.callback_query.filter(F.from_user.id == 243154734)


class Book(StatesGroup):
    name = State()
    price = State()
    cover = State()
    genre = State()


@book_management_router.message(Command("stop"))
@book_management_router.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    print(message.text)
    await state.clear()
    await message.answer("Опрос остановлен")


@book_management_router.message(Command("newbook"), default_state)
async def create_new_book(message: types.Message, state: FSMContext):
    await message.answer("Введите название книги?")
    await state.set_state(Book.name)


@book_management_router.message(Book.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену")
    await state.set_state(Book.price)


@book_management_router.message(Book.price)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Загрузите фото обложки")
    await state.set_state(Book.cover)


@book_management_router.message(Book.cover, F.photo)
async def process_cover(message: types.Message, state: FSMContext):
    covers = message.photo
    pprint(covers)
    biggest_image = covers[-1]
    biggest_image_id = biggest_image.file_id
    await state.update_data(cover=biggest_image_id)
    await message.answer("Введите жанр")
    await state.set_state(Book.genre)


@book_management_router.message(Book.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    data = await state.get_data()
    print(data)
    # сохранение в БД
    database.save_book(data)
    await message.answer("Книга сохранена")
    await state.clear()
