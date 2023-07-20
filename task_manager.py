from reader import Reader
from writer import Writer

class TaskManager:
    def __init__(self, filename):
        self.reader = Reader(filename)

    def delete_task(self):
        """
        Function allows the user to delete a task from a list of tasks by providing
        the task ID.
        """
        all_tasks = self.reader.get_tasks_data()
        if len(all_tasks) < 1:
            print("\n/// There are no tasks to delete \\\\\\")
        else:
            index = 1
            list_of_ids = []
            print("\n/// All tasks \\\\\\")
            for task in all_tasks:
                list_of_ids.append(task["task_id"])
                status = "Active" if task["active"] == "True" else "Inactive"
                print(f"{index}. Task {task['task'].title()}, Task ID: {task['task_id']}, status: {status}")
                index += 1
            while True:
                try:
                    task_id = int(input("\nEnter task id to delete: "))
                    if task_id > 0 and task_id in list_of_ids:
                        break
                    else:
                        print("\n/// Provided task id does not exist \\\\\\\n")
                except ValueError:
                    print("\n/// Invalid input only numbers are allowed \\\\\\\n")
            for task in all_tasks:
                if task["task_id"] == task_id:
                    all_tasks.remove(task)
                    Writer.update_tasks("tasks.json", all_tasks)
                    print(f"\n/// Task deleted \\\\\\")
                    break
            self.delete_task_sub_menu()

    def delete_task_sub_menu(self):
        """
        Function displays a sub-menu with options to delete another task, go
        back to the main menu, or exit the program, and handles the user's choice accordingly.
        """
        from menu import Menu
        while True:
            print("\n1. Delete another task")
            print("2. Back to main menu")
            print("3. Exit")
            try:
                mode = int(input("Mode: "))
                match mode:
                    case 1:
                        self.delete_task()
                    case 2:
                        Menu.select_mode()
                        break
                    case 3:
                        print("Goodbye!")
                        exit()
                    case _:
                        print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")
            except ValueError:
                print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")
                
    def change_status(self):
        """
        Function allows the user to change the status of a task in a task management
        system.
        """
        reader = Reader("tasks.json")
        all_tasks = reader.get_tasks_data()
        if len(all_tasks) == 0:
            print("\n/// There are no tasks to change status \\\\\\")
        else:
            index = 1
            list_of_ids = []
            print("\n/// All tasks \\\\\\")
            for task in all_tasks:
                list_of_ids.append(task["task_id"])
                status = "Active" if task["active"] == "True" else "Inactive"
                print(f"{index}. Task {task['task'].title()}, Task ID: {task['task_id']}, status: {status}")
                index += 1
            while True:
                try:
                    task_id = int(input("\nEnter task id to change status:"))
                    if task_id > 0 and task_id in list_of_ids:
                        break
                    else:
                        print("\n/// Provided task id does not exist \\\\\\\n")
                except ValueError:
                    print("\n/// Invalid input only numbers are allowed \\\\\\\n")
            while True:
                try:
                    print("\n1. Activate task")
                    print("2. Deactivate task")
                    status = int(input("Status: "))
                    if status == 1 or status == 2:
                        break
                    else:
                        print("\n/// Invalid input. Please enter valid number 1 or 2 \\\\\\\n")
                except ValueError:
                    print("\n/// Invalid input only numbers are allowed \\\\\\\n")
            if status == 1:
                status = "True"
            elif status == 2:
                status = "False"     
            
            for task in all_tasks:
                if task["task_id"] == task_id:
                    task["active"] = status
                    Writer.update_tasks("tasks.json", all_tasks)
                    print(f"\n/// Task updated \\\\\\")
                    break
            self.change_status_sub_menu()
    def change_status_sub_menu(self):
        """
        Function displays a sub-menu for changing the status of a task and allows the user to
        select different options.
        """
        from menu import Menu
        while True:
            print("\n1. Change status of another task")
            print("2. Back to main menu")
            print("3. Exit")
            try:
                mode = int(input("Mode: "))
                if mode > 0 and mode < 4:
                    match mode:
                        case 1:
                            self.change_status()
                        case 2:
                            Menu.select_mode()
                            break
                        case 3:
                            print("Goodbye!")
                            exit()
                        case _:
                            print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")
            except ValueError:
                print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")