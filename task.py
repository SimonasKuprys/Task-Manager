from datetime import datetime
import json

class Task:
    def __init__(self,task,priority,description=None):
        """
        The function is a constructor that initializes the attributes of a task object.
        
        :param task: The task parameter is used to store the name or title of the task. It represents
        what needs to be done
        :param priority: The priority parameter is used to indicate the importance or urgency of the
        task. It can be assigned a value such as "high", "medium", or "low" to prioritize tasks
        accordingly
        :param description: The description parameter is an optional parameter that allows you to
        provide additional information or details about the task. It can be used to provide a more
        detailed description of what needs to be done for the task
        """
        
        self.description = description
        self.task = task
        self.active = "True"
        self.priority = priority
        self.task_id = self.task_id()
        
    def to_dict(self):
        """
        Function returns a dictionary representation of an object with attributes such as
        task, description, priority, create_date, active, and task_id.
        :return: a dictionary with the following key-value pairs.
        
        """
        current_date = datetime.now().date().strftime("%Y-%m-%d")
        return {
            "task": self.task,
            "description": self.description,
            "priority": self.priority,
            "create_date": current_date,
            "active": self.active,
            "task_id": self.task_id
        }
    
    def assign_priority(self):
        """
        Function assigns a priority level to an object based on its numerical value.
        """
        if self.priority == 1:
            self.priority = "Low"
        elif self.priority == 2: 
            self.priority = "Medium"
        elif self.priority == 3:
            self.priority = "High"
    
    def task_id(self):
        """
        Function returns a unique task ID by reading a JSON file and finding the next
        available ID.
        :return: a unique task ID. If the "tasks.json" file exists, it reads the file and extracts the
        task IDs from the tasks in the file. It then finds a unique task ID that is not already in the
        list of task IDs and returns it. If the "tasks.json" file does not exist, it returns 1 as the
        default task ID.
        """
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                tasks_id_list = [task["task_id"] for task in tasks]
            unique_task_id = 1
            while unique_task_id in tasks_id_list:
                unique_task_id += 1
            return unique_task_id
        except FileNotFoundError:
            return 1 
        
    