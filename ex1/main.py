from task import Task
from task_manager import TaskManager


if __name__ == "__main__":
    tm1 = TaskManager()
    t1 = Task("Сделать отчет", 5)
    t2 = Task("Купить молоко", 3)
    t3 = Task("Сделать домашнюю работу", 4)
    tm1.add_task(t1)
    tm1.add_more_task(t2, t3)
    # print(tm1)
    # t1.priority = 2
    # print(t1)
    # print(tm1.find_task("Сделать домашнюю работу"))
    # t1.change_status(" canceleD?")
    # print(t1)
    # print(t1 < 5)
