from aiogram import types

from commands.storage.userStorage import Storage
from commands.start import welcome
from databaseFiles.manage.Task.returnableTask import selectData
from databaseFiles.manage.manageDatabase import dataManager

user_storage = Storage()

UPDATE = '/update'
BLANK = ""


class Handle:
    @staticmethod
    async def handle_start_command(message: types.Message):
        await welcome(message)

    @staticmethod
    async def handle_quit_command(message: types.Message):
        await dataManager(message, UPDATE, BLANK)
        await message.answer("You've canceled the action")

    @staticmethod
    async def handle_add_command(message: types.Message, command):
        if command == '/add_task':
            await message.answer("What's the task name?")
            await dataManager(message, UPDATE, command)
        elif not user_storage.check_task(message):
            user_storage.add_task(message)
            await message.answer("What's the task description?")
        elif not user_storage.check_description(message):
            user_storage.add_description(message)
            await user_storage.executeTask(message)
            await dataManager(message, UPDATE, BLANK)
            user_storage.clear(message)

    @staticmethod
    async def handle_remove_command(message: types.Message, command):
        if command == '/remove':
            data = await selectData(message.from_user.id)
            formatted_data = "\n".join(task[0] for task in data) if data else "No tasks found."
            await message.answer(formatted_data)
            await message.answer("What's the task name you want to delete?")
            await dataManager(message, UPDATE, command)
        else:
            await dataManager(message, '/remove', BLANK)
            await dataManager(message, UPDATE, BLANK)

    @staticmethod
    async def handle_show_command(message: types.Message):
        data = await selectData(message.from_user.id)
        formatted_data = ""

        if data:

            for task in data:
                task_name = task[0]
                task_description = task[1]
                formatted_data += f"{task_name} -> {task_description}\n"

            await message.answer("These are all your registered tasks")
        else:
            formatted_data = "No tasks found."

        await message.answer(formatted_data)
