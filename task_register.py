from writer import Writer
from task import Task

class TaskRegister:
    
    def __init__(self):
        pass
    
    def register_task(self):
        """
        Function prompts the user to enter the name, description, and priority of a
        task, validates the input, creates a `Task` object, writes the task to a file, and then calls
        the `register_task_sub_menu` method.
        """
        while True:
            task_name = input("--- Please enter short name of the task: ").title().lstrip()
            if task_name == "" or task_name == " ":
                print("\n/// Invalid input. Please enter task \\\\\\\n")
            else:
                break
        task_description = input("\n--- Description of the task (coud be empty): ").title().lstrip()
        while True:
            try:
                print("\nSelect priority of the task:")
                print("1. Low priority")
                print("2. Medium priority")
                print("3. High priority")
                priority = int(input("Mode: "))
                task = Task(task_name,priority,task_description)
                if priority == 1 or priority == 2 or priority == 3:
                    task.assign_priority()
                    tasks = task.to_dict()
                    Writer.write_to_file("tasks.json", tasks)
                    break
                else:
                    print("\n/// Invalid input. Please enter 1, 2 or 3 \\\\\\")
            except ValueError:
                print("\n/// Invalid input. Please enter 1, 2 or 3 \\\\\\")
        self.register_task_sub_menu()

    def register_task_sub_menu(self):   
        """
        Function displays a menu to the user and allows them to add more
        tasks, go back to the main menu, or exit the program.
        """
        
        while True:
            from menu import Menu
            print("\nAdd one more task?")
            print("1. Yes")
            print("2. Back to menu")
            print("3. Exit")
            try:
                match int(input("Mode: ")):
                    case 1:
                        self.register_task()
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