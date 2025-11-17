class Task:
    name = ''
    id = 0
    done = False
    in_progress = False
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, done={self.done}, in_progress={self.in_progress})"
    
    def __repr__(self):
        return self.__str__()

    def set_done(self):
        if self.in_progress == True:
            self.done = True
    
    def set_in_progress(self):
        self.in_progress = True

    # 1. Implement a to_dict method
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_done": self.done,
            "in_progress": self.in_progress
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data['name'])
        task.id = data['id']
        task.done = data['is_done']
        task.in_progress = data['in_progress']
        return task