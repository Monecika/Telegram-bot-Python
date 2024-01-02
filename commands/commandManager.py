from aiogram import types

from commands.start import welcome
from databaseFiles.manageUser import updateUser, addUser

async def caller(message: types.Message):
    command = message.text.lower()
    if "/" in command:
        if command == '/start':
            await welcome(message)
            await addUser(message, message.from_user.id, "")
        elif command == '/quit':
            await updateUser(message, message.from_user.id, "")
