from enum import Enum

class Status(Enum):
    DONE = 'done'
    IN_PROGRESS = 'in_progress'
    PENDING = 'pending'

class Task:
    name = ''
    id = 0
    status = Status.PENDING
    def __init__(self, name: str, id: int = 0):
        self.name = name
        self.id = id
    
    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, done={self.done}, in_progress={self.in_progress})"
    
    def __repr__(self):
        return self.__str__()

    def set_done(self):
        self.status = Status.DONE
    
    def set_in_progress(self):
        self.status = Status.IN_PROGRESS

    # 1. Implement a to_dict method
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status.value
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data['name'])
        task.id = data['id']
        task.status = Status(data['status'])
        return task