from aiogram import types

from commands.executive.addCommand import Add
from commands.executive.start import welcome
from databaseFiles.manage.manageTasks import selectData, remove
from databaseFiles.manage.manageUser import updateUser

add = Add()


class Handle:
    @staticmethod
    async def handle_start_command(message: types.Message):
        await welcome(message)

    @staticmethod
    async def handle_quit_command(message: types.Message):
        await updateUser(message, message.from_user.id, "")
        message.answer("You've canceled the action")

    @staticmethod
    async def handle_add_command(message: types.Message, command):

        if command == '/add':
            await message.answer("What's the task name?")
            await updateUser(message, message.from_user.id, command)
        elif command != '/add' and add.task is None:
            add.setTask(message.text)
            await message.answer("What's the task description?")
        else:
            add.setDescription(message.text)
            await add.executeTask(message)
            await updateUser(message, message.from_user.id, "")

    @staticmethod
    async def handle_remove_command(message: types.Message, command):
        if command == '/remove':
            data = await selectData(message.from_user.id)
            formatted_data = "\n".join(task[0] for task in data) if data else "No tasks found."
            await message.answer(formatted_data)
            await message.answer("What's the task name you want to delete?")
            await updateUser(message, message.from_user.id, command)
        else:
            await remove(message.text, message.from_user.id, message)
            await updateUser(message, message.from_user.id, "")

    @staticmethod
    async def handle_show_command(message: types.Message):
        data = await selectData(message.from_user.id)
        formatted_data = "\n".join(task[0] for task in data) if data else "No tasks found."
        await message.answer(formatted_data)
        await message.answer("These are all your registered tasks")
