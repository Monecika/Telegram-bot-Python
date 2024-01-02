from aiogram import types

from databaseFiles.manageTasks import addTask


class Add:
    def __init__(self):
        self.task = None
        self.description = None

    def setTask(self, task: str):
        self.task = task

    def setDescription(self, description):
        self.description = description

    async def executeTask(self, message: types.Message):
        await addTask(self.task, self.description, message)
