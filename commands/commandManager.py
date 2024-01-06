from aiogram import types

from commands.handlers import Handle
from databaseFiles.manage.User.returnableUser import doesExist, getMessage
from databaseFiles.manage.manageDatabase import dataManager
handlers = Handle()

BLANK = ""
ADD_USER = '/add_user'


async def caller(message: types.Message):
    command = message.text.lower()
    if not (await doesExist(message.from_user.id)):
        await dataManager(message, ADD_USER, BLANK)

    if command == '/start':
        await handlers.handle_start_command(message)
    elif command == '/quit':
        await handlers.handle_quit_command(message)
    elif command == '/add_task' or (await getMessage(message.from_user.id)) == '/add_task':
        await handlers.handle_add_command(message, command)
    elif command == '/remove' or (await getMessage(message.from_user.id)) == '/remove':
        await handlers.handle_remove_command(message, command)
    elif command == '/show':
        await handlers.handle_show_command(message)
