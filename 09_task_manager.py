import json
import os
from datetime import datetime
from typing import List, Dict

class Task:
    """Represents a single task in the system."""
    def __init__(self, title: str, category: str = "General"):
        self.title = title
        self.category = category
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_completed = False

    def to_dict(self) -> dict:
        """Converts object to dictionary for JSON storage."""
        return self.__dict__

class TaskManager:
    """Handles all logic for managing tasks and file persistence."""
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[dict] = self._load_tasks()

    def _load_tasks(self) -> List[dict]:
        """Private method to load tasks from file with error handling."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not read data file. Starting fresh.")
            return []

    def save_tasks(self):
        """Writes current task list to the JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=4)
        except IOError as e:
            print(f"Critical Error: Could not save data! {e}")

    def add_task(self, title: str, category: str):
        new_task = Task(title, category)
        self.tasks.append(new_task.to_dict())
        self.save_tasks()
        print(f"✔ Task '{title}' added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("\nYour task list is empty. Get some rest!")
            return

        print("\n--- YOUR CURRENT TASKS ---")
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task['is_completed'] else "⏳"
            print(f"{idx}. [{status}] {task['title']} ({task['category']}) - {task['created_at']}")

    def complete_task(self, index: int):
        try:
            self.tasks[index - 1]['is_completed'] = True
            self.save_tasks()
            print("✔ Task marked as complete!")
        except IndexError:
            print("❌ Error: Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        print("\n--- TASK MASTER PRO ---")
        print("1. Add Task\n2. List Tasks\n3. Mark Complete\n4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            title = input("Enter task title: ")
            cat = input("Enter category (default: General): ") or "General"
            manager.add_task(title, cat)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            manager.list_tasks()
            try:
                idx = int(input("Enter task number to complete: "))
                manager.complete_task(idx)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == '4':
            print("Goodbye! Stay productive.")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
