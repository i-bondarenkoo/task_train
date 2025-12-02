from task_queue import TaskQueue
from task_storage import TaskStorage
from task import Task, TaskStatus
import asyncio


class Worker:
    def __init__(self, name: str):
        self.name = name
        self.queue = TaskQueue()
        self.storage = TaskStorage()

    async def run_task(self):

        while True:
            current_task = self.queue.get_task()
            print("Задача выполняется")
            await asyncio.sleep(3)
            print("Выполненеие задачи завершено")
            to_dict = {current_task: "200 ok"}
            self.storage.success.update(to_dict)
