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
    mark_parser = subparsers.add_parser("mark", help="Mark a task")
    mark_parser.add_argument("task_id", type=int)
    mark_parser.add_argument("in-progress", action="store_true", help="Mark done")
    mark_parser.add_argument("done", action="store_true", help="Mark done")
    mark_parser.add_argument("undone", action="store_true", help="Mark pending")

    args = parser.parse_args()

    task_dict = dict()
    file_str=""
    try:
        with open('tasks.json', 'r') as file:
            task_dict = json.load(file)
    except FileNotFoundError:
        print("File was not found. Will create a new one later.")

    match args.command:
        case "list":
            print("Task list may be empty:")
            print(task_dict)
        case "add":
            print("Adding a task")
            newtaskid = len(task_dict)
            task_dict[len(task_dict)] = Task(args.task_name, newtaskid)
        case "mark":
            print("Marking task")
            if args.task_id in task_dict:
                task: Task = task_dict[args.task_id]
                if args.in_progress:
                    task.set_in_progress()
                if args.done:
                    task.set_done()
                if args.undone:
                    task.done = False
            else:
                print(f"Task id {args.task_id} not found")

    # do whatever modification

    print("Writing to tasks.json")

    with open('tasks.json','w') as file:
        json.dump(task_dict, file, default=task_default_serializer, indent=4)