import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from datetime import datetime

class TodoAppAdvancedColoredWelcomeUpdatePrioritized:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced To-Do List")
        self.root.config(bg="#f0f0f0")

        messagebox.showinfo("Welcome!", "Welcome to your Advanced To-Do List!")

        self.tasks = []
        self.selected_index = None 
        self.load_tasks()

        self.task_label = tk.Label(root, text="Task:", bg="#f0f0f0")
        self.task_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.task_entry.focus()

        self.priority_label = tk.Label(root, text="Priority:", bg="#f0f0f0")
        self.priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.priority_var = tk.StringVar(root)
        self.priority_var.set("Normal")
        self.priority_choices = ["High", "Normal", "Low"]
        self.priority_menu = tk.OptionMenu(root, self.priority_var, *self.priority_choices)
        self.priority_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.priority_menu.config(bg="#e0e0e0")

        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):", bg="#f0f0f0")
        self.due_date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.due_date_entry = tk.Entry(root, width=15)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#a0ffa0")
        self.add_button.grid(row=0, column=0, padx=5, sticky="ew")

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, bg="#c0c0ff", state=tk.DISABLED) # Light blue, initially disabled
        self.update_button.grid(row=0, column=1, padx=5, sticky="ew")

        self.task_listbox = tk.Listbox(root, width=50, bg="#f8f8f8")
        self.task_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.task_listbox.bind('<<ListboxSelect>>', self.populate_task_details)

        self.details_frame = tk.LabelFrame(root, text="Task Details", bg="#f0f0f0")
        self.details_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.details_title_label = tk.Label(self.details_frame, text="Title:", bg="#f0f0f0")
        self.details_title_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.details_title_value = tk.Label(self.details_frame, text="", bg="#f0f0f0")
        self.details_title_value.grid(row=0, column=1, padx=5, pady=2, sticky="w")

        self.details_priority_label = tk.Label(self.details_frame, text="Priority:", bg="#f0f0f0")
        self.details_priority_label.grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.details_priority_value = tk.Label(self.details_frame, text="", bg="#f0f0f0")
        self.details_priority_value.grid(row=1, column=1, padx=5, pady=2, sticky="w")

        self.details_due_date_label = tk.Label(self.details_frame, text="Due Date:", bg="#f0f0f0")
        self.details_due_date_label.grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.details_due_date_value = tk.Label(self.details_frame, text="", bg="#f0f0f0")
        self.details_due_date_value.grid(row=2, column=1, padx=5, pady=2, sticky="w")

        self.details_status_label = tk.Label(self.details_frame, text="Status:", bg="#f0f0f0")
        self.details_status_label.grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.details_status_value = tk.Label(self.details_frame, text="", bg="#f0f0f0")
        self.details_status_value.grid(row=3, column=1, padx=5, pady=2, sticky="w")

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_done, bg="#ffffa0")
        self.mark_done_button.grid(row=6, column=0, padx=5, pady=10, sticky="ew")

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ff8080")
        self.delete_button.grid(row=6, column=1, padx=5, pady=10, sticky="ew")

        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(4, weight=1)

        self.update_task_list()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                loaded_tasks = json.load(f)
                self.tasks = []
                for task in loaded_tasks:
                    
                    if 'title' in task and 'done' in task and 'priority' in task:
                        self.tasks.append(task)
                    else:
                        print(f"Warning: Skipping incomplete task: {task}")
        except FileNotFoundError:
                self.tasks = []
        self.sort_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def add_task(self):
        task_title = self.task_entry.get()
        priority = self.priority_var.get()
        due_date_str = self.due_date_entry.get()

        if not task_title:
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        due_date = self.parse_due_date(due_date_str)
        if due_date is None and due_date_str:
            return

        self.tasks.append({"title": task_title, "done": False, "priority": priority, "due_date": due_date})
        self.sort_tasks()
        self.update_task_list()
        self.clear_input_fields()
        self.save_tasks()
        self.disable_update_button()

    def update_task(self):
        if self.selected_index is not None:
            task_title = self.task_entry.get()
            priority = self.priority_var.get()
            due_date_str = self.due_date_entry.get()

            if not task_title:
                messagebox.showwarning("Warning", "Please enter a task.")
                return

            due_date = self.parse_due_date(due_date_str)
            if due_date is None and due_date_str:
                return

            self.tasks[self.selected_index]["title"] = task_title
            self.tasks[self.selected_index]["priority"] = priority
            self.tasks[self.selected_index]["due_date"] = due_date
            self.sort_tasks()
            self.update_task_list()
            self.clear_input_fields()
            self.save_tasks()
            self.disable_update_button()
            self.selected_index = None
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def parse_due_date(self, date_str):
        if not date_str:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid due date format. Please use<ctrl3348>-MM-DD.")
            return None

    def sort_tasks(self):
        priority_order = {"High": 0, "Normal": 1, "Low": 2}
        self.tasks.sort(key=lambda task: (priority_order[task["priority"]], task.get("due_date", None) or ""))

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        priority_prefix = {"High": "1.", "Normal": "2.", "Low": "3."}
        for index, task in enumerate(self.tasks):
            status = "[X]" if task.get("done", False) else "[ ]" # Use .get() with default
            priority_str = priority_prefix.get(task.get("priority", "Normal"), "2.") # Use .get() with default
            title_str = task.get("title", "Untitled Task") # Use .get() with default
            display_text = f"{priority_str} {status} {title_str}"
            if task.get("due_date"):
                display_text += f" (Due: {task['due_date']})"
            self.task_listbox.insert(tk.END, display_text)
            if task.get("done", False):
                self.task_listbox.itemconfig(index, fg="gray", bg="#e8e8e8")
            else:
                self.task_listbox.itemconfig(index, fg="black")

    def populate_task_details(self, event):
        try:
            self.selected_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[self.selected_index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, selected_task.get("title", ""))
            self.priority_var.set(selected_task.get("priority", "Normal"))
            self.due_date_entry.delete(0, tk.END)
            if selected_task.get("due_date"):
                self.due_date_entry.insert(0, selected_task["due_date"])

            self.details_title_value.config(text=selected_task.get("title", ""))
            self.details_priority_value.config(text=selected_task.get("priority", ""))
            self.details_due_date_value.config(text=selected_task.get("due_date", "N/A"))
            status_text = "Done" if selected_task.get("done", False) else "Not Done"
            self.details_status_value.config(text=status_text)

            self.enable_update_button()
        except IndexError:
            self.clear_input_fields()
            self.details_title_value.config(text="")
            self.details_priority_value.config(text="")
            self.details_due_date_value.config(text="")
            self.details_status_value.config(text="")
            self.disable_update_button()
            self.selected_index = None

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["done"] = not self.tasks[selected_index]["done"]
            self.sort_tasks()
            self.update_task_list()
            self.populate_task_details(None)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            deleted_task = self.tasks.pop(selected_index)
            self.sort_tasks()
            self.update_task_list()
            self.populate_task_details(None)
            self.save_tasks()
            messagebox.showinfo("Info", f"Task '{deleted_task['title']}' deleted.")
            self.clear_input_fields()
            self.disable_update_button()
            self.selected_index = None
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_input_fields(self):
        self.task_entry.delete(0, tk.END)
        self.priority_var.set("Normal")
        self.due_date_entry.delete(0, tk.END)

    def enable_update_button(self):
        self.update_button.config(state=tk.NORMAL)

    def disable_update_button(self):
        self.update_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = TodoAppAdvancedColoredWelcomeUpdatePrioritized(root)
    root.mainloop()

if __name__ == "__main__":
    main()