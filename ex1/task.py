from functools import total_ordering
from enum import Enum


class TaskStatus(str, Enum):
    new = "new"
    completed = "completed"
    canceled = "canceled"


@total_ordering
class Task:

    SIMBOLS = " /?,.-"

    def __init__(self, name: str, priority: int = 1):
        Task.verify_priority(priority)
        self.name = name
        self.priority = priority
        self._status = TaskStatus.new

    def __str__(self):
        return f"Задача - {self.name}, приоритет задачи - {self.priority}, статус задачи - {self._status.value}"

    def change_status(self, new_status: str):
        new_status_str = new_status.lower().strip(Task.SIMBOLS)
        try:
            new_status_enum = TaskStatus(new_status_str)
        except Exception:
            raise TypeError("Не корректное значение статуса")
        if self._status == TaskStatus.completed:
            raise ValueError(f"Статус задачи - выполнена, его нельзя изменить")
        self._status = new_status_enum

    @classmethod
    def verify_priority(cls, priority):
        if not 1 <= priority <= 5:
            raise ValueError("Приоритет задачи должен быть в диапазоне от [1-5]")

    @property
    def status(self):
        return self._status.value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Приоритет должен быть от 1 до 5")
        self._priority = value

    def _get_priority(self, other):
        if isinstance(other, Task):
            return other.priority
        elif isinstance(other, int):
            return other
        else:
            raise ValueError("Для сравнения нужно передать Task или int")

    def __eq__(self, other):
        return self.priority == self._get_priority(other)

    def __lt__(self, other):
        return self.priority < self._get_priority(other)


t1 = Task("Сделать отчет", 5)
t2 = Task("Купить молоко", 3)
t3 = Task("Сделать домашнюю работу", 4)

# print(t1)
# t1.change_status(" Completed / ")
# print(t1)

# print(t1 < 1)
# print(1 < t1)
# # print(t2 > 5.5) Ошибка тк сравниваем объект и float
# print(t2 > t3)
# print(t1 == t3)
# print(t1 >= t3)
