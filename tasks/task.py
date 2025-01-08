# tasks/task.py

from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = completed

    def __repr__(self):
        return f"Task({self.title!r}, {self.description!r}, {self.priority!r}, {self.due_date!r}, {self.completed!r})"
    
    def mark_complete(self):
        self.completed = True