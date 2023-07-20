from reader import Reader

class TaskViewer:
    def __init__(self, filename):
        self.reader = Reader(filename)

    def view_all_tasks(self):
        """
        Function displays different options for viewing tasks and prints the
        corresponding tasks based on the user's input.
        """
        all_data = self.reader.get_tasks_data()
        active_tasks = self.reader.get_all_active_tasks()
        priority_tasks = self.reader.get_highest_priority_tasks()
        all_tasks = self.reader.get_all_tasks()

        if len(all_data) < 1:
            print("\n/// There are no tasks to view \\\\\\")
        else:
            while True:
                print("\n===== View tasks =====")
                print("1. All tasks")
                print("2. Active tasks")
                print("3. High priority tasks")

                try:
                    case_for_tasks = int(input("Mode: "))
                    match case_for_tasks:
                        case 1:
                            print(all_tasks)
                            break
                        case 2:
                            print(active_tasks)
                            break
                        case 3:
                            print(priority_tasks)
                            break
                        case _:
                            print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")
                except ValueError:
                    print("\n/// Invalid input. Please enter valid number 1, 2 or 3 \\\\\\")
            self.view_all_tasks_sub_menu()

    def view_all_tasks_sub_menu(self):
        """
        Function displays a sub-menu with options to go back to the tasks
        menu, back to the main menu, or exit the program.
        """
        from menu import Menu
        while True:
            print("\n1. Back to tasks menu")
            print("2. Back to main menu")
            print("3. Exit")
            try:
                mode = int(input("Mode: "))
                match mode:
                    case 1:
                        self.view_all_tasks()
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