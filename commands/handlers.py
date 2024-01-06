from aiogram import types

from commands.executive.addCommand import Add
from commands.executive.start import welcome
from databaseFiles.manage.Task.returnableTask import selectData
from databaseFiles.manage.manageDatabase import dataManager

add = Add()

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
        elif command != '/add_task' and add.task is None:
            add.setTask(message.text)
            await message.answer("What's the task description?")
        else:
            add.setDescription(message.text)
            await add.executeTask(message)
            await dataManager(message, UPDATE, BLANK)

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
