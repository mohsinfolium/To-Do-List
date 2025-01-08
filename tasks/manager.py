# tasks/manager.py

from tasks.task import Task
from tasks.database import Database

class TaskManager:
    def __init__(self):
        self.db = Database()

    def add_task(self, task):
        self.db.save_task(task)

    def get_tasks(self):
        return self.db.load_tasks()

    def mark_task_complete(self, title):
        tasks = self.db.load_tasks()
        for task in tasks:
            if task["title"] == title and not task["completed"]:
                task["completed"] = True
                self.db.save_task(Task(**task))
                break

    def delete_task(self, title):
        tasks = self.db.load_tasks()
        tasks = [task for task in tasks if task["title"] != title]
        self.db.save_all_tasks(tasks)
