from aiogram import types
from databaseFiles.manage.manageDatabase import dataManager

ADD_TASK = '/add_task'
class Add:
    def __init__(self):
        self.task = None
        self.description = None

    def setTask(self, task: str):
        self.task = task

    def setDescription(self, description):
        self.description = description

    async def executeTask(self, message: types.Message):
        params = (message.from_user.id, self.task, self.description)
        await dataManager(message, ADD_TASK, params)
