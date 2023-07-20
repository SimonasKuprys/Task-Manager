from task_manager import TaskManager
from task_register import TaskRegister
from email_sender import EmailSender
from task_viewer import TaskViewer


class Menu:
    @staticmethod
    def select_mode():
        """
        Function presents a menu to the user and allows them to perform various
        tasks related to managing tasks, such as adding new tasks, viewing tasks, sending tasks to
        email, changing task status, deleting tasks, or exiting the program.
        """
        task_manager = TaskManager("tasks.json")
        task_register = TaskRegister()
        tasks_to_email = EmailSender("tasks.json")
        all_tasks = TaskViewer("tasks.json")
        while True:
            print("\n===== MENU =====")
            print("1. Add new task")
            print("2. View tasks")
            print("3. Get tasks to email")
            print("4. Change task status")
            print("5. Delete task")
            print("6. Exit")
            try:
                user_mode: int = int(input("Mode: "))
                match user_mode:
                    case 1:
                        task_register.register_task()
                    case 2:
                        all_tasks.view_all_tasks()
                    case 3:
                        tasks_to_email.send_tasks_to_email()
                    case 4:
                        task_manager.change_status()
                    case 5:
                        task_manager.delete_task()
                    case 6:
                        print("Goodbye!")
                        exit()
                    case _:
                        print("\n/// Invalid input. Please enter 1 to 6 \\\\\\\n")
            except ValueError:
                print("\n/// Invalid input. Please enter 1 to 6 \\\\\\\n")
        