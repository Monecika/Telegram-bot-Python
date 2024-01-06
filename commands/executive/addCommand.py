from aiogram import types
from databaseFiles.manage.manageDatabase import dataManager



class Add:
    def __init__(self):
        self.user_id = user_id
        self.task = None
        self.description = None

    def setUserId(self, user_id: str):
        self.user_id = user_id

    def setTask(self, task: str):
        self.task = task

    def setDescription(self, description):
        self.description = description

    async def executeTask(self, message: types.Message):
        params = (message.from_user.id, self.task, self.description)
        await dataManager(message, ADD_TASK, params)
