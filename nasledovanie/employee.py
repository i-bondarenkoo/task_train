from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass
