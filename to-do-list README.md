# Advanced To-Do List Application

This is a feature-rich To-Do List application built using Python and the Tkinter GUI library. It allows you to manage your tasks effectively with prioritization, due dates, and status tracking.

## Features

* **Add Tasks:** Easily add new tasks with a title, priority level (High, Normal, Low), and an optional due date.
* **Task Prioritization:** Assign priority levels to your tasks, and they will be visually ordered in the list with numbered prefixes (1. High, 2. Normal, 3. Low).
* **Due Dates:** Set due dates for your tasks in the YYYY-MM-DD format to stay on schedule. Invalid date formats will trigger an error message.
* **Mark as Done:** Toggle the status of a task as "Done," which will visually gray out the task in the list.
* **Delete Tasks:** Remove tasks from your list when they are completed or no longer needed.
* **Update Tasks:** Select a task from the list, modify its title, priority, or due date in the input fields, and click "Update Task" to save the changes.
* **Persistent Storage:** Your tasks are saved to a `tasks.json` file in the same directory as the script, ensuring your list persists between application sessions.
* **Welcome Message:** A friendly welcome message greets you when you launch the application.
* **Task Details:** Selecting a task in the listbox displays its full details (title, priority, due date, status) in a dedicated section.
* **Colored Interface:** A simple color scheme enhances the visual appeal and usability of the application.

## How to Run

1.  **Prerequisites:** Ensure you have Python installed on your system. Tkinter comes standard with most Python installations.
2.  **Download the Script:** Save the provided Python code as a `.py` file (e.g., `todo_app.py`).
3.  **Run from Terminal:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command:
    ```bash
    python todo_app.py
    ```
    This will launch the To-Do List application window.

## How to Use

1.  **Adding a Task:**
    * Enter the task description in the "Task:" entry field.
    * Select the priority from the "Priority:" dropdown menu.
    * Optionally, enter the due date in the "Due Date (YYYY-MM-DD):" entry field.
    * Click the "Add Task" button.

2.  **Marking a Task as Done:**
    * Select the task you want to mark as done from the listbox.
    * Click the "Mark as Done" button. The task will be visually updated in the list.

3.  **Deleting a Task:**
    * Select the task you want to delete from the listbox.
    * Click the "Delete Task" button. A confirmation message will appear.

4.  **Updating a Task:**
    * Select the task you want to update from the listbox. Its details will be populated in the input fields.
    * Modify the "Task," "Priority," or "Due Date" as needed.
    * Click the "Update Task" button to save your changes. The "Update Task" button is only enabled when a task is selected.

## File Storage

The application uses a file named `tasks.json` to store your to-do list data. This file will be created in the same directory where you run the `todo_app.py` script. You should not manually edit this file unless you understand its structure, as it could lead to errors in the application.

## Potential Future Enhancements

* **Task Editing Directly in List:** Allow users to edit tasks by double-clicking on them in the list.
* **Due Date Reminders:** Implement notifications or visual cues for approaching due dates.
* **Task Categories or Tags:** Add the ability to categorize or tag tasks for better organization.
* **Recurring Tasks:** Support for tasks that repeat on a regular basis (daily, weekly, etc.).
* **More Advanced Sorting and Filtering:** Allow users to sort tasks by due date, priority, or status, and filter tasks based on criteria.
* **User Interface Improvements:** Further refine the visual design and layout of the application.

Enjoy managing your tasks with this advanced To-Do List application!
