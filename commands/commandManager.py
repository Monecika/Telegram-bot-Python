from aiogram import types

from commands.addCommand import Add
from commands.start import welcome
from databaseFiles.manageUser import updateUser, addUser, getMessage

add = Add()


async def caller(message: types.Message):
    command = message.text.lower()
    await addUser(message, message.from_user.id, "")

    if command == '/start':
        await welcome(message)
    elif command == '/quit':
        await updateUser(message, message.from_user.id, "")
    elif command == '/add' or (await getMessage(message.from_user.id)) == '/add':
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