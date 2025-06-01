import json
import os

TODO_FILE = 'todo.json'


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    for i, task in enumerate(tasks, start=1):
        status = '✅' if task['done'] else '❌'
        print(f"{i}. {status} {task['title']}")


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({'title': title, 'done': False})
        print("Task added.")


def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()

