from aiogram import Router, F

from .book_management import book_management_router
from .books_shop import shop_router
from .dialog import opros_router
from .other_messages import echo_router
from .picture import picture_router
from .start import start_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(picture_router)
private_router.include_router(book_management_router)
private_router.include_router(opros_router)
private_router.include_router(shop_router)

# в самом конце
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == "private")
private_router.callback_query.filter(F.chat.type == "private")
