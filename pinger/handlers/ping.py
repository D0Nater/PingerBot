"""Ping handler."""

from time import perf_counter

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("ping"))
async def ping_command(message: Message) -> None:
    """Ping handler."""
    start_time = perf_counter()
    m = await message.answer("<b>Ping!</b>")
    finish_time = perf_counter()
    ping_time = finish_time - start_time
    await m.edit_text(f"<b>Pong {ping_time:.3f}s!</b>")
