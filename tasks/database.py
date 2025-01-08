# tasks/database.py

import json
import os
from tasks.task import Task

class Database:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def save_task(self, task):
        tasks = self.load_tasks()
        tasks.append({
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "due_date": task.due_date.strftime("%Y-%m-%d"),
            "completed": task.completed
        })
        with open(self.filename, "w") as f:
            json.dump(tasks, f)

    def save_all_tasks(self, tasks):
        with open(self.filename, "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        with open(self.filename, "r") as f:
            tasks_data = json.load(f)
        return tasks_data
