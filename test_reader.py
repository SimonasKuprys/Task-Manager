from reader import Reader
from writer import Writer
import os

INFO = {"task": "Test", "description": "Test", "priority": "High", "create_date": "2023-07-19", "active": "True","task_id": 2}

def test_get_tasks_data(info=INFO):
    filename = "test_task.json"
    Writer.write_to_file(filename, info)
    reader = Reader(filename)
    assert reader.get_tasks_data() == [info]
    os.remove(filename)
    
def test_get_all_tasks(info=INFO):
    filename = "test_task.json"
    Writer.write_to_file(filename, info)
    reader = Reader(filename)
    assert reader.get_all_tasks() == "\n/// All tasks \\\\\\ \n1. Task: Test, Description: Test, Task ID: 2\n/// End of tasks \\\\\\"
    os.remove(filename)

def test_get_all_active_tasks(info=INFO):
    filename = "test_task.json"
    Writer.write_to_file(filename, info)
    reader = Reader(filename)
    assert reader.get_all_active_tasks() == "\n/// Active tasks \\\\\\ \n1. Task: Test, Description: Test, Task ID: 2\n/// End of tasks \\\\\\"
    os.remove(filename)
    
def test_get_highest_priority_tasks(info=INFO):
    filename = "test_task.json"
    Writer.write_to_file(filename, info)
    reader = Reader(filename)
    assert reader.get_highest_priority_tasks() == "\n/// Highest active priority tasks \\\\\\ \n1. Task: Test, Description: Test, Task ID: 2\n/// End of tasks \\\\\\"
    os.remove(filename)

def test_get_tasks_data_file_not_found(info=INFO):
    filename = "test_task.json"
    reader = Reader(filename)
    assert reader.get_tasks_data() == []
    
def test_get_all_tasks_file_not_found(info=INFO):
    filename = "test_task.json"
    reader = Reader(filename)
    assert reader.get_all_tasks() == []
    
def test_get_all_active_tasks_file_not_found(info=INFO):
    filename = "test_task.json"
    reader = Reader(filename)
    assert reader.get_all_active_tasks() == []
    
def test_get_highest_priority_tasks_file_not_found(info=INFO):
    filename = "test_task.json"
    reader = Reader(filename)
    assert reader.get_highest_priority_tasks() == []