#!/usr/bin/env python3
"""
Interactive Task Manager Application
A simple command-line task management system with menu-driven interface.
"""

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        """Add a new task to the list."""
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{description}' added successfully!")

    def view_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        print("-" * 40)
        for task in self.tasks:
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{task['id']}. {status} {task['description']}")
        print("-" * 40)

    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"Task {task_id} is already completed.")
                else:
                    task['completed'] = True
                    print(f"Task '{task['description']}' marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed_task = self.tasks.pop(i)
                print(f"Task '{removed_task['description']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("         INTERACTIVE TASK MANAGER")
    print("="*50)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")
    print("="*50)

def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main application loop."""
    manager = TaskManager()

    print("Welcome to the Interactive Task Manager!")
    print("Manage your tasks efficiently with this simple application.")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            description = input("Enter task description: ").strip()
            if description:
                manager.add_task(description)
            else:
                print("Task description cannot be empty.")

        elif choice == 2:
            manager.view_tasks()

        elif choice == 3:
            if not manager.tasks:
                print("No tasks available to complete.")
                continue
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == 4:
            if not manager.tasks:
                print("No tasks available to delete.")
                continue
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == 5:
            print("Thank you for using the Task Manager. Goodbye!")
            break

        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()