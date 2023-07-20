from writer import Writer
from task_manager import TaskManager
import json
import os

def test_write_to_file():
    """
    Function tests the `write_to_file` method of the `Writer` class.
    """
    file_name = "test_task.json"
    info = {"task": "Test", "description": "Test", "priority": "High", "create_date": "2023-07-19", "active": "True","task_id": 2}
    Writer.write_to_file(file_name, info)
    with open(file_name, "r") as file:
        tasks = json.load(file)
    assert tasks == [info]
    os.remove(file_name)
    
# def test_delete_from_file():
#     """
#     Function tests the `delete_from_file` method of the `Writer` class.
#     """
#     file_name = "test_task.json"
#     info = {"task": "Test", "description": "Test", "priority": "High", "create_date": "2023-07-19", "active": "True","task_id": 2}
#     Writer.write_to_file(file_name, info)
#     task_manager = TaskManager(file_name)
#     task_manager.delete_task()
#     with open(file_name, "r") as file:
#         tasks = json.load(file)
#     assert tasks == []
#     os.remove(file_name)