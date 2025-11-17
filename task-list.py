import argparse
import json
from Task import Task

def task_default_serializer(obj: Task):
    # 2. Check the type and call the conversion method
    if isinstance(obj, Task):
        print("is instance of task")
        return obj.to_dict()
    print("not instance of task")
    # Let the default encoder handle other types it knows how to serialize
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Gestor CLI de tareas")

    subparsers = parser.add_subparsers(title="command", dest='command')

    # -----------------------
    # Subcomand: list
    # -----------------------
    list_parser = subparsers.add_parser("list", help="List tasks")
    # (list no necesita más args)

    # -----------------------
    # Subcomand: add
    # -----------------------
    list_parser = subparsers.add_parser("add", help="Add a task")
    list_parser.add_argument("task_name", type=str, help="Task name")

    # -----------------------
    # Subcomand: update
    # -----------------------
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("task_id", type=int, help="Task id")

    # -----------------------
    # Subcomand: mark
    # -----------------------
    mark_parser = subparsers.add_parser("mark", help="Marca una tarea como hecha o pendiente")
    mark_parser.add_argument("task_id", type=int)
    mark_parser.add_argument("--done", action="store_true", help="Marcar como hecha")
    mark_parser.add_argument("--undone", action="store_true", help="Marcar como pendiente")

    args = parser.parse_args()

    task_dict = dict()
    file_str=""
    try:
        with open('tasks.json', 'r') as file:
            all_tasks_dict = json.load(file)
            for task_data in all_tasks_dict:
                task = Task.from_dict(task_data)
                task_dict[task.id] = task
    except FileNotFoundError:
        print("File was not found. Will create a new one later.")

    print(f"Task dict status: {task_dict}")

    match args.command:
        case "list":
            print("Task list may be empty:")
            for t in task_dict:
                print(f"ID: {t['id']} - Name: {t['name']} - Done: {t['done']} - In Progress: {t['in_progress']}")
        case "add":
            print("Adding a task")
            task_dict[len(task_dict)] = Task(args.task_name)

    # do whatever modification

    print(task_dict)
    print("Writing to tasks.json")

    with open('tasks.json','w') as file:
        json_output = str()
        if len(task_dict) > 0:
            for (k,v) in task_dict.items():
                json_output += json.dumps(v,default=task_default_serializer)
        file.write(json_output)