from enum import Enum


class TaskType(str, Enum):
    download = "download"
    process = "process"
    compute = "compute"


class TaskStatus(str, Enum):
    pending = "pending"
    running = "running"
    done = "done"
    failed = "failed"


class Task:
    id_counter = 0

    def __init__(
        self,
        type: TaskType,
        payload: dict | None = None,
    ):
        self.id = Task.generate_id()
        self.type = type
        self._status = TaskStatus.pending
        self.payload = payload

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: TaskStatus):
        if not isinstance(value, TaskStatus):
            raise TypeError("Статус должен относиться к классу TaskStatus")
        self._status = value

    @classmethod
    def generate_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def __str__(self):
        return f"Task(id={self.id}, type={self.type}, status={self.status}, payload={self.payload})"
