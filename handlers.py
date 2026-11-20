from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="openpulse")


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "سلام! به OpenPulse AI خوش آمدی.\n"
        "این نسخه اولیه ربات است. قابلیت‌های خبری در مراحل بعد اضافه می‌شوند.\n"
        "برای راهنما /help را بفرست."
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "OpenPulse AI — راهنما\n"
        "/start — شروع ربات\n"
        "/help — نمایش راهنما\n\n"
        "در نسخه فعلی فقط دستورات پایه فعال‌اند."
    )
