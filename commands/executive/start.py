from aiogram import types


async def welcome(message: types.Message):
    introduction = ("Hello! I'm your task manager bot. You can use the following commands:\n"
                    "/start - Start the bot and see this message\n"
                    "/quit - Quit the current operation\n"
                    "/add_task - Add a new task\n"
                    "/remove - Remove an existing task\n"
                    "/show - Show all your tasks")

    await message.answer(introduction)
