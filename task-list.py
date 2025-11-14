import argparse
import json

class task:
    name = ''
    id = 0
    done = False
    in_progress = False
    def task(self, name):
        self.name = name

    def set_done(self):
        if self.in_progress == True:
            self.done = True
    
    def set_in_progress(self):
        self.in_progress = True

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Gestor CLI de tareas")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # -----------------------
    # Subcomando: list
    # -----------------------
    list_parser = subparsers.add_parser("list", help="Lista las tareas")
    # (list no necesita más args)

    # -----------------------
    # Subcomando: update
    # -----------------------
    update_parser = subparsers.add_parser("update", help="Actualiza una tarea")
    update_parser.add_argument("task_id", type=int, help="ID de la tarea")
    update_parser.add_argument("--text", "-t", required=True, help="Nuevo texto")

    # -----------------------
    # Subcomando: mark
    # -----------------------
    mark_parser = subparsers.add_parser("mark", help="Marca una tarea como hecha o pendiente")
    mark_parser.add_argument("task_id", type=int)
    mark_parser.add_argument("--done", action="store_true", help="Marcar como hecha")
    mark_parser.add_argument("--undone", action="store_true", help="Marcar como pendiente")

    args = parser.parse_args()

    task_list = dict()
    file_str=""
    print("a")
    with open('tasks.json', 'r') as file:
        file_str = file.read()
    task_list = json.JSONDecoder.decode(file_str)

    task_list.update(update)
    # do whatever modification

    task_list_json_output = json.JSONEncoder.encode(task_list)

    with open('tasks.json','w') as file:
        file.write(task_list_json_output)