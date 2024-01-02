import asyncio

from aiogram import types

from commands.commandManager import caller
from config import dp, bot


@dp.message()
async def start(message: types.Message):
    await caller(message)


async def startup():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(startup())
