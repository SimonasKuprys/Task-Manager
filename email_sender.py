from reader import Reader
from mail import Mail

class EmailSender:
    def __init__(self, filename):
        self.reader = Reader(filename)
        
    def send_tasks_to_email(self):
        """
        Function prompts the user to select a mode (1, 2, or 3) and sends the
        corresponding tasks to an email using the `Mail.send_email` method.
        """
        reader = Reader("tasks.json")
        all_data = self.reader.get_tasks_data()
        active_tasks = reader.get_all_active_tasks()
        priority_tasks = reader.get_highest_priority_tasks()
        all_tasks = reader.get_all_tasks()
        if len(all_data) < 1:
            print("\n/// There are no tasks to send \\\\\\")
        else:
            while True:
                print("\nWhich tasks do you want to send to email?")
                print("1. All tasks")
                print("2. All active tasks")
                print("3. All highest priority tasks")
                try:
                    mode = int(input("Mode: "))
                    match mode:
                        case 1:
                            Mail.send_email(all_tasks)
                            break
                        case 2:
                            Mail.send_email(active_tasks)
                            break
                        case 3:
                            Mail.send_email(priority_tasks)
                            break
                        case _:
                            print("\n/// Invalid input. Please enter 1, 2 or 3 \\\\\\")
                except ValueError:
                    print("\n/// Invalid input. Please enter 1, 2 or 3 \\\\\\")
            self.send_tasks_to_email_sub_menu()
                
    def send_tasks_to_email_sub_menu(self):
        """
        Function displays a sub-menu with options to send more tasks
        to email, go back to the main menu, or exit the program.
        """
        from menu import Menu
        while True:
            print("\nSend more tasks to email?")
            print("1. Yes")
            print("2. Back to menu")
            print("3. Exit")
            try:
                match int(input("Mode: ")):
                    case 1:
                        self.send_tasks_to_email()
                    case 2:
                        Menu.select_mode()
                        break
                    case 3:
                        print("Goodbye!")
                        exit()
                    case _:
                        print("\n/// Invalid input. Please enter valid number \\\\\\")
            except ValueError:
                print("\n/// Invalid input. Please enter valid number \\\\\\")