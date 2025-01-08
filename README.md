# Command Line Interface To-Do App

This is a simple command-line interface (CLI) To-Do List app built using Python. It allows you to manage your tasks efficiently through various commands such as adding, listing, completing, and deleting tasks.

The app is designed with the following functionalities:

- Add tasks with details like title, description, priority, and due date.
- List all tasks along with their current status (Pending/Completed).
- Mark tasks as completed.
- Delete tasks from the list.

## Features

- **Add tasks**: You can add new tasks with a title, description, priority (1-5), and due date.
- **List tasks**: View all your tasks with their title, status (Pending/Completed), priority, and due date.
- **Complete tasks**: Mark tasks as completed.
- **Delete tasks**: Delete tasks from the list.

## File Structure

```
todo_app/
├── main.py                # Entry point for the application
├── tasks/
│   ├── __init__.py        # Makes the folder a Python package
│   ├── task.py            # Defines the Task class
│   ├── manager.py         # Handles CRUD operations for tasks
│   └── database.py        # Handles saving/loading tasks to/from JSON
├── cli/
│   ├── __init__.py        # Makes the folder a Python package
│   ├── interface.py       # Handles user input and CLI commands
├── data/
│   └── tasks.json         # Stores tasks in JSON format (for persistence)
└── README.md              # Documentation about the app
```

## Installation

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your system.
3. Install any necessary dependencies (if required).

```bash
# Navigate to the project directory
cd /path/to/your/project

# Install dependencies (if needed)
# pip install -r requirements.txt  # If you have a requirements.txt file
```

## Usage

### Add a Task

To add a new task, use the following command:

```bash
python3 main.py add --title "Task Title" --description "Task Description" --priority 3 --due-date "2025-01-10"
```

### List All Tasks

To view all tasks, run:

```bash
python3 main.py list
```

### Mark a Task as Completed

To mark a task as completed, use:

```bash
python3 main.py complete --title "Task Title"
```

### Delete a Task

To delete a task, run:

```bash
python3 main.py delete --title "Task Title"
```

## Testing the App

After running the app, you can test the following commands:

1. **Add a task**:
   ```bash
   python3 main.py add --title "Buy groceries" --description "Milk, eggs, bread" --priority 2 --due-date "2025-01-10"
   ```
2. **List tasks**:

   ```bash
   python3 main.py list
   ```

3. **Complete a task**:

   ```bash
   python3 main.py complete --title "Buy groceries"
   ```

4. **Delete a task**:
   ```bash
   python3 main.py delete --title "Buy groceries"
   ```

## JSON Storage

The tasks are stored in a `tasks.json` file located in the `data` directory. The app uses this file for persistence, so even after you close the application, your tasks will remain stored and accessible the next time you run the app.
