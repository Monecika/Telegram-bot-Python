from aiogram import types

from databaseFiles.manage.taskHandler import TaskHandle

ADD_TASK = '/add_task'


class Storage:
    def __init__(self):
        self.task_list = []
        self.description_list = []

    def add_task(self, message: types.Message):
        self.task_list.append({message.from_user.id: message.text})

    def add_description(self, message: types.Message):
        self.description_list.append({message.from_user.id: message.text})

    def check_task(self, message: types.Message):
        for task_dist in self.task_list:
            if message.from_user.id in task_dist:
                return True
        return False

    def check_description(self, message: types.Message):
        for description_dict in self.description_list:
            if message.from_user.id in description_dict:
                return True
        return False

    def get_task(self, message: types.Message):
        user_id = message.from_user.id

        for task_dict in self.task_list:
            if user_id in task_dict:
                return task_dict[user_id]

    def get_description(self, message: types.Message):
        user_id = message.from_user.id

        for description_dict in self.description_list:
            if user_id in description_dict:
                return description_dict[user_id]

    def clear(self, message: types.Message):
        user_id = message.from_user.id

        for task_dict in self.task_list:
            if user_id in task_dict:
                self.task_list.remove(task_dict)

        for description_dict in self.description_list:
            if user_id in description_dict:
                self.description_list.remove(description_dict)

    async def executeTask(self, message: types.Message):
        query = {"_id": message.from_user.id, "TaskName": self.get_task(message),
                 "TaskDescription": self.get_description(message)}
        await TaskHandle.handle_AddTask(message, query)
