import json

class Reader:
    def __init__(self, filename):
        self.filename = filename

    def get_tasks_data(self):
        """
        Function reads data from a file and returns it as a dictionary, or an empty
        dictionary if the file is not found.
        :return: the data read from the file in JSON format. If the file is not found, it will print an
        error message and return an empty list.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            # print(f"\n /// File not found \\\\\\")
            return []

    def get_all_tasks(self):
        """
        Function reads a JSON file, extracts task information, and returns a
        formatted string containing all the tasks.
        :return: a string that contains all the tasks stored in a file. Each task is formatted with its
        index, task name, description, and task ID. The string also includes a header and footer to
        indicate the start and end of the tasks. If the file is not found, an empty list is returned.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                tasks = [
                    f"{index + 1}. Task: {item['task'].title()}, Description: {item['description']}, Task ID: {item['task_id']}"
                    for index, item in enumerate(data)
                ]
                string = "\n/// All tasks \\\\\\ \n" + "\n".join(tasks) + "\n/// End of tasks \\\\\\"
                return string
        except FileNotFoundError:
            # print(f"\n /// File not found \\\\\\")
            return []
        
    def get_all_active_tasks(self):
        """
        Function reads data from a file, filters out active tasks, and
        returns a formatted string of the active tasks.
        :return: a string that contains the list of active tasks. If there are no active tasks, it
        returns a string indicating that there are no active tasks. If the file is not found, it returns
        a string indicating that the file was not found.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
            index = 1
            active_tasks = []
            for item in data:
                if item.get("active") == "True":
                    string = f"{index}. Task: {item['task'].title()}, Description: {item['description']}, Task ID: {item['task_id']}"
                    active_tasks.append(string)
                    index += 1
        except FileNotFoundError:
            # print(f"\n /// File not found \\\\\\")
            return []
        if active_tasks == []:
            return "\n/// No active tasks \\\\\\"
        else:
            active_tasks_string = "\n/// Active tasks \\\\\\ \n" + "\n".join(active_tasks) + "\n/// End of tasks \\\\\\"
            return active_tasks_string
        
    def get_highest_priority_tasks(self):
        """
        Function retrieves the highest priority tasks from a JSON file and returns them as a
        formatted string.
        :return: a string that contains the highest priority tasks. If the file is not found, it returns
        the message "File not found". If there are no active high priority tasks, it returns the message
        "No active high priority tasks". Otherwise, it returns a string that lists the highest priority
        tasks.
        """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                index = 1
                highest_priority_tasks = []
                for item in data:
                    if item.get("priority") == "High" and item.get("active") == "True":
                        string = f"{index}. Task: {item['task'].title()}, Description: {item['description']}, Task ID: {item['task_id']}"
                        highest_priority_tasks.append(string)
                        index += 1
        except FileNotFoundError:
            # print(f"\n /// File not found \\\\\\")
            return []
        if highest_priority_tasks == []:
            return "\n/// No active high priority tasks \\\\\\"
        else:
            highest_priority_string = "\n/// Highest active priority tasks \\\\\\ \n" + "\n".join(highest_priority_tasks) + "\n/// End of tasks \\\\\\"
            return highest_priority_string