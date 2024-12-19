from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


review_router = Router()
users = []

class Review(StatesGroup):
    name = State()


@review_router.callback_query(F.data == "review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id in users:
        await callback.message.answer("You have revied us already")
        return
    users.append(callback.from_user.id)
    await callback.answer()
    await callback.message.answer("Как вас зовут?")
    await state.set_state(Review.name)