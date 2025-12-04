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
            current_task = await self.queue.get_task()
            print("Задача выполняется")
            current_task.status = TaskStatus.running
            await asyncio.sleep(3)
            current_task.status = TaskStatus.done
            print("Выполненеие задачи завершено")
