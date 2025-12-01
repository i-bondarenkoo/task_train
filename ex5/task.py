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
    id = 0

    def __init__(
        self,
        id: int,
        type: TaskType,
        status: TaskStatus,
        payload: dict | None = None,
    ):
        self.id = id
        self.type = type
        self.status = status
        self.payload = payload

    def __str__(self):
        return f"Task(id={self.id}, type={self.type}, status={self.status}, payload={self.payload})"
