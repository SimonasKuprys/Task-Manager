import json

class Writer:
    @staticmethod
    def write_to_file(filename, info):
        """
        Function reads a JSON file, appends new information to it, and then writes
        the updated information back to the file.
        """
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        tasks.append(info)
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"Task successfully added.\n")
        
    @staticmethod
    def update_tasks(filename,updated_info):
        """
        Function updates the contents of a file with the provided updated information
        in JSON format.
        """
        try:
            with open(filename, "w") as file:
                json.dump(updated_info, file, indent=4)
        except FileNotFoundError:    
            print(f"File '{filename}' not found.")
            return "File not found."
