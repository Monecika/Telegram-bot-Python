from aiogram import types


async def welcome(message: types.Message):
    introduction = "Welcome to TaskManagerBot!\n\n" \
                   "I'm here to help you manage your tasks. Here are some available commands:\n" \
                   "/add_task <task_description> - Add a new task\n" \
                   "/view_tasks - View your task list\n" \
                   "/remove_task <task_number> - Remove a task\n" \
                   "\nGet organized and stay on top of your tasks with TaskManagerBot!"

    await message.answer(introduction)