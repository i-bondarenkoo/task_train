class Task:
    def __init__(self, name: str, priority: int = 1):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Задача - {self.name}, приоритет задачи - {self.priority}"

    def __lt__(self, other):
        if not isinstance(other, Task):
            raise TypeError("Можно сравнивать только объекты класса Task")
        return self.priority < other.priority


t1 = Task("Сделать отчет", 5)
t2 = Task("Купить молоко", 3)
t3 = Task("Сделать домашнюю работу", 4)

print(t1 > t3)
