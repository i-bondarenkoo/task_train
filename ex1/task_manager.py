from unittest import result
from task import Task, t1, t2, t3


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("Передан не верный объект")
        for elem in self.tasks:
            if task.name == elem.name:
                raise ValueError("Такая задача уже существует")
        self.tasks.append(task)

    def add_more_task(self, *task: Task):
        names = {e.name for e in self.tasks}
        for elements in task:
            if elements.name in names:
                raise ValueError("Такая задача уже есть")
            self.tasks.append(elements)
            names.add(elements.name)

    def get_high_priority_tasks(self, min_priority: int = 3):
        return [str(task) for task in self.tasks if task.priority >= min_priority]

    def find_task(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        result = [task for task in self.tasks if task.name == name]
        if not result:
            raise ValueError(f"Задача '{name}' не найдена")
        return result[0]

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)


# tm1 = TaskManager()
# print("---")
# tm1.add_task(t1)
# # print(tm1)
# tm1.add_more_task(t2, t3)
# # print(tm1)
# print(tm1.get_high_priority_tasks(5))
# # print("---------------")
# # print(tm1.find_task("Сделать домашнюю работу"))
