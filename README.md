Python To-Do List

A command-line To-Do List application built with Python. This project allows users to manage tasks and store them permanently using file handling.

Features

- Add Task
- View Tasks
- Mark Task as Completed
- Update Tasks
- Delete Tasks
- Persistent File Storage
- Exit Program

Task Information

Each task contains:

- Task Name
- Deadline
- Additional Information
- Status (Pending / Completed)

Concepts Used

This project was built to practice:

- Variables
- User Input
- Conditional Statements
- Loops
- File Handling
- Reading Files
- Writing Files
- Updating File Contents
- CRUD Operations

How It Works

Add Task:
Users can add a new task by entering:
- Task name
- Deadline
- Additional information

The task is automatically assigned a status of Pending and saved to a text file.

View Tasks:
Displays all tasks stored in the file.

Mark Task Completed:
Updates the status of a selected task from Pending to Completed.

Update Task:
Allows users to modify:
- Task name
- Deadline
- Information
- Status

Delete Task:
Removes a task from the file permanently.

Exit:
Closes the application.

File Storage:

Tasks are stored in a text file (task.txt).

Unlike the previous version, tasks remain saved even after the program is closed and reopened.

Example Menu:

text 1. Add Task 2. View Task 3. Mark Task Completed 4. Update Task 5. Delete Task 6. Exit 

How to Run:

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run:

bash python todo_list.py 

Future Improvements:

- Functions for cleaner code
- Exception handling
- Task priorities
- Task categories
- Search tasks
- Graphical User Interface (GUI)

Author
Manoj M

Built as a Python learning project to practice file handling and CRUD operations.
