from aiogram import types

from databaseFiles.manage.Task.noReturnableTask import executeTask
from databaseFiles.manage.User.noReturnableUser import executeUser

ADD_USER = f"""
            INSERT INTO Users(UserId, LastMessage)
            VALUES (?, ?)
    """

UPDATE = f"""
                UPDATE Users 
                SET LastMessage = ?
                WHERE UserId = ?
    """

REMOVE = f"""
        DELETE FROM Task WHERE
        TaskName = ? and UserId = ?
    """

ADD_TASK = f"""
        INSERT INTO Task VALUES
        (?, ?, ?)
    """

TEXT_ADD_TASK = "Task was added successfully"
TEXT_REMOVE_TASK = "Task deleted successfully"


async def dataManager(message: types.Message, task, command):
    if task == '/update':
        params = (command, message.from_user.id)
        await executeUser(UPDATE, params)
    elif task == '/add_user':
        params = (message.from_user.id, command)
        await executeUser(ADD_USER, params)
    elif task == '/remove':
        params = (message.text, message.from_user.id)
        await executeTask(message, REMOVE, params, TEXT_REMOVE_TASK)
    elif task == '/add_task':
        await executeTask(message, ADD_TASK, command, TEXT_ADD_TASK)
