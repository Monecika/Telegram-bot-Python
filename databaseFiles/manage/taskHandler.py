from aiogram import types

from commandConfiguration import Commands
from databaseFiles.database import Users, Tasks


class TaskHandle:
    @staticmethod
    async def getUserID(message: types.Message):
        return message.from_user.id

    @staticmethod
    async def handle_find(message: types.Message):
        user_id = await TaskHandle.getUserID(message)

        result = Users.find_one({Commands.ID: user_id})
        return bool(result)

    @staticmethod
    async def handle_LastMessage(message: types.Message):
        user_id = await TaskHandle.getUserID(message)

        result = Users.find_one({Commands.ID: user_id})
        return result[Commands.LAST_MESSAGE]

    @staticmethod
    async def handle_Update(message: types.Message, command):
        user_id = await TaskHandle.getUserID(message)
        old_user = {Commands.ID: user_id}
        new_user = {"$set": {Commands.LAST_MESSAGE: command}}
        Users.update_one(old_user, new_user)

    @staticmethod
    async def handle_AddUser(message: types.Message, command):
        user_id = await TaskHandle.getUserID(message)
        user = {Commands.ID: user_id, Commands.LAST_MESSAGE: command}
        Users.insert_one(user)

    @staticmethod
    async def handle_Remove(message: types.Message):
        user_id = await TaskHandle.getUserID(message)

        Tasks.delete_one({Commands.ID: user_id, Commands.TASK_NAME: message.text})
        await message.answer(Commands.TEXT_REMOVE_TASK)

    @staticmethod
    async def handle_AddTask(message: types.Message, query):
        Tasks.insert_one(query)
        await message.answer(Commands.TEXT_ADD_TASK)

    @staticmethod
    async def handle_Show(message: types.Message):
        user_id = await TaskHandle.getUserID(message)
        user_tasks = []

        for document in Tasks.find({Commands.ID: user_id}):
            user_tasks.append(document[Commands.TASK_NAME])

        if user_tasks:
            await message.answer('\n'.join(map(str, user_tasks)))
            await message.answer("These are all of your tasks")
        else:
            await message.answer("You don't have any tasks yet")
