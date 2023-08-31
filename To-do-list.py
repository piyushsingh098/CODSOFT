import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database initialization
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
conn.commit()

def add_task():
    task = task_entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task:
            task_id = selected_task_index[0] + 1
            cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
            conn.commit()
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to update.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task_id = selected_task_index[0] + 1
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        tasks_listbox.delete(selected_task_index)

def load_tasks():
    cursor.execute("SELECT task FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        tasks_listbox.insert(tk.END, task[0])

# Create the main application window
app = tk.Tk()
app.title("To-Do List App")

# Create and place widgets
task_entry = tk.Entry(app)
task_entry.pack(padx=10, pady=10, fill=tk.BOTH)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5, fill=tk.BOTH)

update_button = tk.Button(app, text="Update Selected Task", command=update_task)
update_button.pack(padx=10, pady=5, fill=tk.BOTH)

remove_button = tk.Button(app, text="Remove Selected Task", command=remove_task)
remove_button.pack(padx=10, pady=5, fill=tk.BOTH)

tasks_listbox = tk.Listbox(app)
tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

load_tasks()

app.mainloop()

# Close the database connection when the application is closed
conn.close()