from task import Task
import asyncio


class TaskQueue:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("Передан не верный объект")
        await self.queue.put(task)

    async def get_task(self):

        current_task = await self.queue.get()
        return current_task
