# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def display_menu():
    """Display the menu options."""
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    """Add a task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """View the list of tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_complete():
    """Mark a task as complete."""
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_index] += " (X)"
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def delete_task():
    """Delete a task from the list."""
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
