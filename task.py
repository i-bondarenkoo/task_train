from functools import total_ordering


@total_ordering
class Task:
    def __init__(self, name: str, priority: int = 1):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Задача - {self.name}, приоритет задачи - {self.priority}"

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

print(t1 < 1)
print(1 < t1)
# print(t2 > 5.5) Ошибка тк сравниваем объект и float
print(t2 > t3)
print(t1 == t3)
print(t1 >= t3)
