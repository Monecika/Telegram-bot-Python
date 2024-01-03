from aiogram import types

from commands.handlers import Handle
from databaseFiles.manage.manageUser import addUser, getMessage

handlers = Handle()


async def caller(message: types.Message):
    command = message.text.lower()
    await addUser(message, message.from_user.id, "")
    if command == '/start':
        await handlers.handle_start_command(message)
    elif command == '/quit':
        await handlers.handle_quit_command(message)
    elif command == '/add' or (await getMessage(message.from_user.id)) == '/add':
        await handlers.handle_add_command(message, command)
    elif command == '/remove' or (await getMessage(message.from_user.id)) == '/remove':
        await handlers.handle_remove_command(message, command)
    elif command == '/show':
        await handlers.handle_show_command(command)
