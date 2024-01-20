from aiogram import types

from commandConfiguration import Commands
from commands.handlers import Handle
from databaseFiles.manage.taskHandler import TaskHandle

Task_handle = TaskHandle()
handlers = Handle()


async def caller(message: types.Message):
    if not await Task_handle.handle_find(message):
        await Task_handle.handle_AddUser(message, Commands.BLANK)

    command = message.text.lower()
    lastMessage = await Task_handle.handle_LastMessage(message)

    if command == Commands.START:
        await handlers.handle_start_command(message)
    elif command == Commands.QUIT:
        await handlers.handle_quit_command(message)
    elif command == Commands.ADD_TASK or lastMessage == Commands.ADD_TASK:
        await handlers.handle_add_command(message, command)
    elif command == Commands.REMOVE_TASK or lastMessage == Commands.REMOVE_TASK:
        await handlers.handle_remove_command(message, command)
    elif command == Commands.SHOW:
        await Task_handle.handle_Show(message)
