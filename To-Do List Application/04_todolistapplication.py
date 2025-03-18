def add_task(task):
    tasks.append(task)
    save_tasks()

def view_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def delete_task(index):
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks()
    else:
        print("Invalid task index.")

def mark_task_as_done(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = f"[DONE] {tasks[index - 1]}"
        save_tasks()
    else:
        print("Invalid task index.")

def save_tasks():
    with open("To-Do List Application/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("To-Do List Application/tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

tasks = load_tasks()

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to delete: "))
        delete_task(index)
    elif choice == "4":
        index = int(input("Enter the task index to mark as done: "))
        mark_task_as_done(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")

save_tasks()