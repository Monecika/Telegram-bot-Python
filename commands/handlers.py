from aiogram import types

from commandConfiguration import Commands
from commands.start import welcome
from commands.storage.userStorage import Storage
from databaseFiles.manage.taskHandler import TaskHandle

Task_handle = TaskHandle()

user_storage = Storage()


class Handle:
    @staticmethod
    async def handle_start_command(message: types.Message):
        await welcome(message)

    @staticmethod
    async def handle_quit_command(message: types.Message):
        await Task_handle.handle_Update(message, Commands.BLANK)
        if not await Task_handle.handle_LastMessage(message):
            await message.answer("You've canceled the action")

    @staticmethod
    async def handle_add_command(message: types.Message, command):
        if command == Commands.ADD_TASK:
            await message.answer("What's the task name?")
            await Task_handle.handle_Update(message, command)
        elif not user_storage.check_task(message):
            user_storage.add_task(message)
            await message.answer("What's the task description?")
        elif not user_storage.check_description(message):
            user_storage.add_description(message)
            await user_storage.executeTask(message)
            await Task_handle.handle_Update(message, Commands.BLANK)
            user_storage.clear(message)

    @staticmethod
    async def handle_remove_command(message: types.Message, command):
        if command == Commands.REMOVE_TASK:
            await Task_handle.handle_Show(message)
            await message.answer("What's the task name you want to delete?")
            await Task_handle.handle_Update(message, command)
        else:
            await Task_handle.handle_Remove(message)
            await Task_handle.handle_Update(message, Commands.BLANK)
