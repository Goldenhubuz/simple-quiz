import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found!")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✗"
            print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added successfully!")

def remove_task(tasks):
    """Remove a task."""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[index]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main loop of the CLI app."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
