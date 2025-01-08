# cli/interface.py

import argparse
from tasks.manager import TaskManager
from tasks.task import Task

def list_tasks(args):
    manager = TaskManager()
    tasks = manager.get_tasks()
    if tasks:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"{task['title']} - {status} (Priority: {task['priority']}, Due: {task['due_date']})")
    else:
        print("No tasks available.")

def add_task(title, description, priority, due_date):
    manager = TaskManager()
    task = Task(title, description, priority, due_date)
    manager.add_task(task)
    print(f"Task '{title}' added.")

def complete_task(title):
    manager = TaskManager()
    manager.mark_task_complete(title)
    print(f"Task '{title}' marked as completed.")

def delete_task(title):
    manager = TaskManager()
    manager.delete_task(title)
    print(f"Task '{title}' deleted.")

def main():
    parser = argparse.ArgumentParser(description="Manage your to-do list.")
    subparsers = parser.add_subparsers(help="sub-command help")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--title", required=True, help="Title of the task")
    add_parser.add_argument("--description", required=True, help="Description of the task")
    add_parser.add_argument("--priority", required=True, type=int, help="Priority of the task (1-5)")
    add_parser.add_argument("--due-date", required=True, help="Due date of the task (YYYY-MM-DD)")
    add_parser.set_defaults(func=lambda args: add_task(args.title, args.description, args.priority, args.due_date))

    # List tasks command
    subparsers.add_parser("list", help="List all tasks").set_defaults(func=list_tasks)

    # Complete task command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("--title", required=True, help="Title of the task")
    complete_parser.set_defaults(func=lambda args: complete_task(args.title))

    # Delete task command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("--title", required=True, help="Title of the task")
    delete_parser.set_defaults(func=lambda args: delete_task(args.title))

    args = parser.parse_args()
    args.func(args)